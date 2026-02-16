import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
from io import BytesIO

# ── Configuração da página ──────────────────────────────────────────────────
st.set_page_config(
    page_title="Análise de Correlação",
    page_icon="📊",
    layout="wide",
)

# ── CSS customizado ─────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@300;400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Source Sans 3', sans-serif;
    }
    .block-container { padding-top: 2rem; }
    
    .main-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #1a1a2e;
        margin-bottom: 0.2rem;
        letter-spacing: -0.5px;
    }
    .subtitle {
        font-size: 1rem;
        color: #6c757d;
        margin-bottom: 1.5rem;
    }
    .section-header {
        font-size: 1.05rem;
        font-weight: 600;
        color: #1a1a2e;
        border-bottom: 2px solid #e63946;
        padding-bottom: 0.3rem;
        margin-bottom: 1rem;
    }
    .metric-card {
        background: #f8f9fa;
        border-radius: 8px;
        padding: 1rem 1.2rem;
        border-left: 4px solid #e63946;
        margin-bottom: 0.5rem;
    }
    .metric-label { font-size: 0.8rem; color: #6c757d; text-transform: uppercase; letter-spacing: 0.5px; }
    .metric-value { font-size: 1.4rem; font-weight: 700; color: #1a1a2e; }
    
    div[data-testid="stSidebar"] {
        background: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# AUTENTICAÇÃO
# As credenciais ficam nos Secrets do Streamlit Cloud (não no código).
# No painel do app: Settings > Secrets, cole:
#   [passwords]
#   mauricio = "SuaSenhaForte123"
#   cliente1 = "OutraSenha456"
# ══════════════════════════════════════════════════════════════════════════════

def verificar_credenciais(usuario, senha):
    """Verifica login contra os Secrets do Streamlit Cloud."""
    try:
        senhas = st.secrets["passwords"]
        if usuario in senhas and senhas[usuario] == senha:
            return True
    except (KeyError, FileNotFoundError):
        st.error("⚠️ Secrets não configurados. Configure [passwords] nos Secrets do Streamlit Cloud.")
    return False


def tela_login():
    """Exibe formulário de login centralizado."""
    # Esconde sidebar antes do login
    st.markdown("<style>section[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown("")
        st.markdown("")
        st.markdown('<div class="main-title" style="text-align:center;">📊 Análise de Correlação</div>', unsafe_allow_html=True)
        st.markdown('<div class="subtitle" style="text-align:center;">Faça login para acessar</div>', unsafe_allow_html=True)
        
        with st.form("login_form"):
            usuario = st.text_input("Usuário")
            senha = st.text_input("Senha", type="password")
            submit = st.form_submit_button("Entrar", use_container_width=True)
            
            if submit:
                if verificar_credenciais(usuario, senha):
                    st.session_state["autenticado"] = True
                    st.session_state["usuario"] = usuario
                    st.rerun()
                else:
                    st.error("Usuário ou senha incorretos.")


# Controle de sessão
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

if not st.session_state["autenticado"]:
    tela_login()
    st.stop()


# ══════════════════════════════════════════════════════════════════════════════
# APP PRINCIPAL (só aparece após login)
# ══════════════════════════════════════════════════════════════════════════════

# ── Cabeçalho ───────────────────────────────────────────────────────────────
st.markdown('<div class="main-title">📊 Análise de Correlação</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Carregue seus dados, selecione variáveis e método, e explore as correlações.</div>', unsafe_allow_html=True)

# ── Sidebar ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(f"👤 **{st.session_state['usuario']}**")
    if st.button("Sair", use_container_width=True):
        st.session_state["autenticado"] = False
        st.session_state["usuario"] = ""
        st.rerun()
    
    st.markdown("---")
    st.markdown('<div class="section-header">📁 Dados</div>', unsafe_allow_html=True)
    arquivo = st.file_uploader("Carregar arquivo Excel", type=["xlsx", "xls"], help="Arquivo .xlsx ou .xls com dados numéricos")
    
    if arquivo is not None:
        try:
            df = pd.read_excel(arquivo)
            st.success(f"{df.shape[0]} linhas × {df.shape[1]} colunas")
        except Exception as e:
            st.error(f"Erro ao ler arquivo: {e}")
            st.stop()
    else:
        st.info("Envie um arquivo Excel para começar.")
        st.stop()

    cols_numericas = df.select_dtypes(include=[np.number]).columns.tolist()
    
    if len(cols_numericas) < 2:
        st.error("O arquivo precisa ter ao menos 2 colunas numéricas.")
        st.stop()

    st.markdown("---")
    st.markdown('<div class="section-header">⚙️ Configuração</div>', unsafe_allow_html=True)
    
    metodo = st.selectbox(
        "Método de correlação",
        ["pearson", "spearman", "kendall"],
        format_func=lambda x: {
            "pearson": "Pearson (paramétrico, linear)",
            "spearman": "Spearman (não-paramétrico, ranks)",
            "kendall": "Kendall (não-paramétrico, amostras pequenas)"
        }[x],
        help="Pearson: relação linear, dados normais. Spearman: monotônica, sem normalidade. Kendall: amostras pequenas ou empates."
    )
    
    st.markdown("---")
    st.markdown('<div class="section-header">📌 Variáveis</div>', unsafe_allow_html=True)
    
    vars_independentes = st.multiselect(
        "Variáveis independentes (X)",
        cols_numericas,
        help="Ex.: variáveis de saneamento, preditoras"
    )
    
    cols_restantes = [c for c in cols_numericas if c not in vars_independentes]
    
    vars_dependentes = st.multiselect(
        "Variáveis dependentes (Y)",
        cols_restantes,
        help="Ex.: variáveis de doenças, resposta"
    )

    if not vars_independentes or not vars_dependentes:
        st.warning("Selecione ao menos 1 variável em cada grupo.")
        st.stop()

    st.markdown("---")
    st.markdown('<div class="section-header">🎨 Visual</div>', unsafe_allow_html=True)
    paleta = st.selectbox("Paleta de cores", ["RdBu_r", "coolwarm", "PiYG", "BrBG", "PRGn", "RdYlGn"], index=0)
    alpha = st.select_slider("Nível de significância (α)", options=[0.01, 0.05, 0.10], value=0.05)


# ── Funções auxiliares ──────────────────────────────────────────────────────

def calcular_correlacao(df, vars_x, vars_y, metodo):
    corr_func = {
        "pearson": stats.pearsonr,
        "spearman": stats.spearmanr,
        "kendall": stats.kendalltau
    }[metodo]
    
    mat_r = pd.DataFrame(index=vars_x, columns=vars_y, dtype=float)
    mat_p = pd.DataFrame(index=vars_x, columns=vars_y, dtype=float)
    mat_n = pd.DataFrame(index=vars_x, columns=vars_y, dtype=int)
    
    for x in vars_x:
        for y in vars_y:
            validos = df[[x, y]].dropna()
            n = len(validos)
            mat_n.loc[x, y] = n
            if n > 2:
                r, p = corr_func(validos[x], validos[y])
                mat_r.loc[x, y] = r
                mat_p.loc[x, y] = p
            else:
                mat_r.loc[x, y] = np.nan
                mat_p.loc[x, y] = np.nan
    
    return mat_r, mat_p, mat_n


def formatar_tabela(mat_r, mat_p, alpha):
    tabela = pd.DataFrame(index=mat_r.index, columns=mat_r.columns)
    for x in mat_r.index:
        for y in mat_r.columns:
            r = mat_r.loc[x, y]
            p = mat_p.loc[x, y]
            if pd.notna(p):
                if p < 0.001:
                    sig = "***"
                elif p < 0.01:
                    sig = "**"
                elif p < alpha:
                    sig = "*"
                else:
                    sig = "ns"
                tabela.loc[x, y] = f"{r:.3f} {sig}"
            else:
                tabela.loc[x, y] = "NA"
    return tabela


def criar_heatmap(mat_r, mat_p, alpha, paleta, metodo):
    fig, ax = plt.subplots(figsize=(max(6, len(mat_r.columns) * 1.5), max(4, len(mat_r.index) * 1.0)))
    
    annot = mat_r.copy().astype(object)
    for x in mat_r.index:
        for y in mat_r.columns:
            r = mat_r.loc[x, y]
            p = mat_p.loc[x, y]
            if pd.notna(r) and pd.notna(p):
                if p < 0.001:
                    sig = "***"
                elif p < 0.01:
                    sig = "**"
                elif p < alpha:
                    sig = "*"
                else:
                    sig = ""
                annot.loc[x, y] = f"{r:.2f}{sig}"
            else:
                annot.loc[x, y] = "NA"
    
    sns.heatmap(
        mat_r.astype(float),
        annot=annot, fmt="",
        cmap=paleta, center=0, vmin=-1, vmax=1,
        square=True, linewidths=0.8, linecolor="#ffffff",
        cbar_kws={"label": f"Correlação ({metodo.capitalize()})", "shrink": 0.8},
        ax=ax, annot_kws={"size": 10}
    )
    
    nomes_metodo = {"pearson": "Pearson (r)", "spearman": "Spearman (ρ)", "kendall": "Kendall (τ)"}
    ax.set_title(f"Matriz de Correlação — {nomes_metodo[metodo]}", fontsize=13, fontweight="bold", pad=14)
    ax.set_xlabel("Variáveis Dependentes", fontsize=10, fontweight="bold")
    ax.set_ylabel("Variáveis Independentes", fontsize=10, fontweight="bold")
    ax.tick_params(axis='x', rotation=45, labelsize=9)
    ax.tick_params(axis='y', rotation=0, labelsize=9)
    fig.text(0.5, -0.02, f"*** p<0.001   ** p<0.01   * p<{alpha}   (sem asterisco = não significativo)", 
             ha="center", fontsize=8, color="#6c757d")
    fig.tight_layout()
    return fig


# ── Cálculos ────────────────────────────────────────────────────────────────
mat_r, mat_p, mat_n = calcular_correlacao(df, vars_independentes, vars_dependentes, metodo)
tabela_formatada = formatar_tabela(mat_r, mat_p, alpha)

# ── Métricas ────────────────────────────────────────────────────────────────
n_total = mat_n.values.flatten()
n_sig = ((mat_p.astype(float) < alpha) & mat_p.notna()).sum().sum()
n_pares = mat_r.notna().sum().sum()
r_abs_max = mat_r.astype(float).abs().max().max() if mat_r.notna().any().any() else 0

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f'<div class="metric-card"><div class="metric-label">Pares analisados</div><div class="metric-value">{n_pares}</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="metric-card"><div class="metric-label">Significativos (p&lt;{alpha})</div><div class="metric-value">{n_sig}</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div class="metric-card"><div class="metric-label">Maior |r|</div><div class="metric-value">{r_abs_max:.3f}</div></div>', unsafe_allow_html=True)
with col4:
    n_obs_med = int(np.nanmedian(n_total)) if len(n_total) > 0 else 0
    st.markdown(f'<div class="metric-card"><div class="metric-label">N mediano</div><div class="metric-value">{n_obs_med}</div></div>', unsafe_allow_html=True)

st.markdown("")

# ── Tabs ────────────────────────────────────────────────────────────────────
tab_fig, tab_tabela, tab_pval, tab_dados = st.tabs(["🔥 Heatmap", "📋 Tabela Formatada", "📐 P-valores", "🗂️ Dados Brutos"])

with tab_fig:
    fig = criar_heatmap(mat_r, mat_p, alpha, paleta, metodo)
    st.pyplot(fig, use_container_width=False)
    buf_fig = BytesIO()
    fig.savefig(buf_fig, format="png", dpi=300, bbox_inches="tight", facecolor="white")
    buf_fig.seek(0)
    st.download_button("⬇️ Baixar figura (PNG)", buf_fig, file_name="correlacao_heatmap.png", mime="image/png")

with tab_tabela:
    st.markdown(f"Coeficientes de correlação com indicação de significância (α = {alpha})")
    st.dataframe(tabela_formatada, use_container_width=True)
    st.caption(f"*** p<0.001 · ** p<0.01 · * p<{alpha} · ns = não significativo")

with tab_pval:
    st.markdown("Matriz de p-valores")
    st.dataframe(mat_p.astype(float).style.format("{:.4f}").background_gradient(cmap="Reds_r", vmin=0, vmax=0.1), use_container_width=True)

with tab_dados:
    st.markdown("Pré-visualização dos dados carregados (colunas selecionadas)")
    st.dataframe(df[vars_independentes + vars_dependentes].head(50), use_container_width=True)

# ── Exportação Excel ────────────────────────────────────────────────────────
st.markdown("---")
st.markdown('<div class="section-header">📥 Exportar Resultados</div>', unsafe_allow_html=True)

buf_excel = BytesIO()
with pd.ExcelWriter(buf_excel, engine="openpyxl") as writer:
    mat_r.to_excel(writer, sheet_name="Correlacoes")
    mat_p.to_excel(writer, sheet_name="P-valores")
    mat_n.to_excel(writer, sheet_name="N_observacoes")
    tabela_formatada.to_excel(writer, sheet_name="Tabela_Formatada")
buf_excel.seek(0)

st.download_button(
    "⬇️ Baixar resultados (Excel)",
    buf_excel,
    file_name="resultados_correlacao.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

st.markdown("---")
st.caption("Análise de Correlação · Pearson | Spearman | Kendall · Desenvolvido com Streamlit")
