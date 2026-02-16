---
# **ANÁLISE DE AÇÕES DA BOLSA DE VALORES DO BRASIL (B3)**
---

Nesse notebook vamos listar uma série de indicadores disponíveis no Yahoo Finance, os quais podem nos auxiliar no estudo de ações de interesse.

Importante ressaltar que não sou economista, investidor profissional ou agende financeiro, sou apenas um curioso, apaixonado por ciência de dados, que sempre está buscando uma forma de por a ciência de dados em prática, com dados reais, e o assunto de hoje é a análise de ações da bolsa de valores.

Vamos usar aqui a biblioteca **yfinance**. O yfinance não é afiliado, ou verificado pelo Yahoo, é apenas uma ferramenta de código aberto que usa APIs disponíveis publicamente do Yahoo e se destina a fins educacionais e de pesquisa.

# **O que estudaremos aqui?**

Dividi o conteúdo em aglomerados de índices/informações que julguei estarem melhor representados juntos:

- Preços, Metas e Recomendações
- Dividendos
- Desempenho Histórico
- Composição das ações
- Índices financeiros
- Volume e Liquidez
- Margens e Valuation
- Valor contábil e de Mercado
- Riscos
- Análise Financeira
- Desempenho Financeiro
- Margens e Fluxo de Caixa
- Crescimento

---

# **Preços, Metas e Recomendações**

1. 'currentPrice':Preço atual da ação.
2. 'targetHighPrice': Meta de preço alta definida pelos analistas.
3. 'targetLowPrice': Meta de preço baixa definida pelos analistas.
4. 'targetMeanPrice': Média das metas de preço definidas pelos analistas.
5. 'targetMedianPrice': Mediana das metas de preço definidas pelos analistas.
6. 'recommendationMean': Média das recomendações dos analistas (1=Comprar, 2=Manter, 3=Vender).
7. 'recommendationKey': Recomendação geral dos analistas.

# **Dividendos**

1. previousClose: Preço de fechamento anterior
2. regularMarketPreviousClose: Preço de fechamento regular do mercado anterior
3. dividendRate: Taxa de dividendos
4. dividendYield: Rendimento de dividendos
5. exDividendDate: Data de ex-dividendo (formato Unix)
6. 'trailingAnnualDividendRate': Taxa de dividendos anuais (últimos 12 meses)
7. 'trailingAnnualDividendYield': Rendimento de dividendos anuais (últimos 12 meses)
8. payoutRatio: Razão de pagamento de dividendos
9. fiveYearAvgDividendYield: Yield médio de dividendos dos últimos 5 anos

# **Desempenho Histórico**

1. 'fiftyTwoWeekHigh': Maior preço nos últimos 52 semanas
2. 'fiftyDayAverage': Média móvel de 50 dias
3. 'twoHundredDayAverage': Média móvel de 200 dias

# **Composição das ações**

1. 'floatShares': Número de ações flutuantes
2. 'sharesOutstanding': Número total de ações emitidas
3. 'impliedSharesOutstanding': Número estimado de ações emitidas (potencial)
4. 'heldPercentInsiders': Percentual de ações detidas por insiders (diretoria e funcionários)
5. 'heldPercentInstitutions': Percentual de ações detidas por instituições financeiras

# **Índices Financeiros**

1. beta:Medida de volatibilidade de uma ação em relação ao mercado como um todo.

- Valor de 1: Volatilidade igual à do mercado.
- Valor > 1: Volatilidade maior que a do mercado.
- Valor < 1: Volatilidade menor que a do mercado.

2. trailingPE: P/L (Preço/Lucro) trailing (últimos 12 meses)

- O P/E trailing mede o preço atual da ação dividido pelo lucro por ação (LPA) dos últimos 12 meses.
- Indica se a ação está sendo negociada a um preço justo em relação ao seu desempenho.
- Valor baixo: Ação pode estar subvalorizada.
- Valor alto: Ação pode estar sobrevalorizada.

3. forwardPE: P/L forward (próximos 12 meses)

- O P/E forward mede o preço atual da ação dividido pelo lucro por ação (LPA) estimado para os próximos 12 meses.
- Indica as expectativas de crescimento da empresa.
- Valor baixo: Expectativas de crescimento baixas.
- Valor alto: Expectativas de crescimento altas.
- No caso, o P/E forward de 4,26 sugere que o mercado espera um crescimento moderado na lucratividade da PETR4.

# **Volume e Liquidez**

1. averageVolume: 33.589.556 - Volume médio
2. averageVolume10days: 27.164.810 - Volume médio dos últimos 10 dias
3. averageDailyVolume10Day: 27.164.810 - Volume médio diário dos últimos 10 dias

# **Margens e Valuation**

1. 'profitMargins': Margem de lucro
2. 'priceToSalesTrailing12Months': Preço/Venda (últimos 12 meses)
3. 'priceToBook': Preço/Livro (valor contábil)

# **Valor contábil e de Mercado**

1. 'marketCap': Valor de mercado da empresa (capitalização de mercado)
2. 'enterpriseValue': Valor da empresa
3. 'bookValue': Valor contábil por ação.
4. 'priceToBook': Preço/Valor Contábil (P/B).
5. 'enterpriseToRevenue': Valor da empresa dividido pela receita.
6. 'enterpriseToEbitda': Valor da empresa dividido pelo EBITDA.

# **Riscos**

## 1. AuditRisk: Risco de Auditoria

- Avalia o risco de irregularidades ou erros nos relatórios financeiros da empresa.
- Considera fatores como:
- Qualidade da auditoria.
- Histórico de erros ou irregularidades.
- Mudanças na equipe de auditoria.
- Nível de risco:
- 1-2: Baixo
- 3-5: Médio
- 6-10: Alto

## 2. BoardRisk: Risco da Diretoria

- Avalia o risco relacionado à composição e desempenho da diretoria da empresa.
- Considera fatores como:
- Experiência e habilidades dos diretores.
- Independência e diversidade da diretoria.
- Histórico de decisões questionáveis.
- Nível de risco:
- 1-2: Baixo
- 3-5: Médio
- 6-10: Alto

## 3. CompensationRisk: Risco de Remuneração

- Avalia o risco relacionado à estrutura de remuneração dos executivos da empresa.
- Considera fatores como:
- Alinhamento entre remuneração e desempenho.
- Transparência e justiça na remuneração.
- Risco de perda de talentos.
- Nível de risco:
- 1-2: Baixo
- 3-5: Médio
- 6-10: Alto

## 4. ShareHolderRightsRisk: Risco dos Direitos dos Acionistas

- Avalia o risco relacionado à proteção dos direitos dos acionistas.
- Considera fatores como:
- Estrutura de governança.
- Direitos de voto.
- Transparência e comunicação.
- Nível de risco:
- 1-2: Baixo
- 3-5: Médio
- 6-10: Alto

## 5. OverallRisk: Risco Geral

- Avalia o risco total associado à empresa.
- Considera fatores como:
- Risco financeiro.
- Risco operacional.
- Risco de mercado.
- Risco regulatório.
- Nível de risco:
- 1-2: Baixo
- 3-5: Médio
- 6-10: Alto

# **Análise Financeira**

1. 'numberOfAnalystOpinions': 10 - Número de opiniões de analistas.
2. 'totalCash': 67.676.999.680 - Total de caixa da empresa.
3. 'totalCashPerShare': 5,251 - Caixa por ação.
4. 'ebitda': 225.348.993.024 - Lucro antes de juros, impostos, depreciação e amortização.
5. 'totalDebt': 331.472.994.304 - Total de dívida da empresa.
6. 'quickRatio': 0,605 - Razão rápida (ativos circulantes/dívidas curtas).
7. 'currentRatio': 0,895 - Razão corrente (ativos circulantes/dívidas curtas).

# **Desempenho Financeiro**

1. 'totalRevenue': 499.064.995.840 - Receita total da empresa.
2. 'debtToEquity': 88,148 - Razão dívida/patrimônio.
3. 'revenuePerShare': 38,524 - Receita por ação.
4. 'returnOnAssets': 0,1122 - Retorno sobre ativos.
5. 'returnOnEquity': 0,21172 - Retorno sobre patrimônio.

# **Margens e Fluxo de Caixa**

1. 'grossMargins': 0,52235 - Margem bruta.
2. 'ebitdaMargins': 0,45154 - Margem EBITDA.
3. 'operatingMargins': 0,30754998 - Margem operacional.
4. 'freeCashflow': 108.373.377.024 - Fluxo de caixa livre.
5. 'operatingCashflow': 207.837.003.776 - Fluxo de caixa operacional.

# **Crescimento**

'revenueGrowth': 0,074 - Crescimento da receita.

---

# **AGORA VAMOS AO CÓDIGO:**

Para tornar o estudo das ações mais prático, até mesmo porque essa é uma ferramenta que pretendo usar corriqueiramente, preferi por estruturar meu código de forma que a análise seja exportada em um arquivo PDF, respeitando os tópicos citados no texto acima, assim posso gerar o relatório das minhas ações de interesse, e vou analisando os PDFs conforme tenho tempo durante o dia.

## **LEMBRE-SE DE SUBSTITUIR O TICKET DA AÇÃO DE INTERESSE EM "ticker = yf.Ticker('PETR4.SA')".**

```
# Importar bibliotecas necessárias

import yfinance as yf
from fpdf import FPDF
import pandas as pd

# Definir o ticker da ação PETR4 - nesse exemplo usei PETROBRAS, usar sempre ".SA" após o ticket padrão da ação.

ticker = yf.Ticker('PETR4.SA')

# Imprimir as informações

info = ticker.info

# Criar um objeto PDF

pdf = FPDF()

# Adicionar página

pdf.add_page()

# Definir fonte e tamanho

pdf.set_font("Arial", size = 15)

# Função para adicionar tópico

def adiciona_topico(titulo):
pdf.set_font("Arial", style='B', size = 15)
pdf.cell(200, 10, txt = titulo, ln = True, align = 'C')
pdf.ln(10)
pdf.set_font("Arial", size = 12)

# Cotações e recomendações

adiciona_topico("Cotações e Recomendações")
pdf.cell(200, 10, txt = f"Preço atual: {info.get('currentPrice', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Preço-alvo alto: {info.get('targetHighPrice', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Preço-alvo baixo: {info.get('targetLowPrice', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Preço-alvo médio: {info.get('targetMeanPrice', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Preço-alvo mediano: {info.get('targetMedianPrice', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Média da recomendação dos analistas: {info.get('recommendationMean', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Recomendação dos analistas: {info.get('recommendationKey', 'Não encontrado')}", ln = True, align = 'L')
pdf.ln(10)

# Preços e dividendos

adiciona_topico("Preços e Dividendos")
pdf.cell(200, 10, txt = f"Taxa de dividendos: {info.get('dividendRate', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Rendimento de dividendos: {info.get('dividendYield', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Data de ex-dividendo (formato Unix): {info.get('exDividendDate', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Taxa de dividendos anuais (últimos 12 meses): {info.get('trailingAnnualDividendRate', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Rendimento de dividendos anuais (últimos 12 meses): {info.get('trailingAnnualDividendYield', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Razão de pagamento de dividendos: {info.get('payoutRatio', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Yield médio de dividendos dos últimos 5 anos: {info.get('fiveYearAvgDividendYield', 'Não encontrado')}", ln = True, align = 'L')
pdf.ln(10)

# Desempenho Histórico

adiciona_topico("Desempenho Histórico")
pdf.cell(200, 10, txt = f"Maior preço nos últimos 52 semanas: {info.get('fiftyTwoWeekHigh', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Média móvel de 50 dias: {info.get('fiftyDayAverage', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Média móvel de 200 dias: {info.get('twoHundredDayAverage', 'Não encontrado')}", ln = True, align = 'L')
pdf.ln(10)

# Composição das ações

adiciona*topico("Composição das Ações")
pdf.cell(200, 10, txt = f"Número de ações flutuantes: {info.get('floatShares', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Número total de ações emitidas: {info.get('sharesOutstanding', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Número estimado de ações emitidas (potencial): {info.get('impliedSharesOutstanding', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Percentual de ações detidas por insiders (diretoria e funcionários): {round(info.get('heldPercentInsiders', 0) * 100, 2)}%", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Percentual de ações detidas por instituições financeiras: {round(info.get('heldPercentInstitutions', 0) \_ 100, 2)}%", ln = True, align = 'L')
pdf.ln(10)

# Preços e dividendos

adiciona_topico("Preços e Dividendos")
pdf.cell(200, 10, txt = f"Taxa de dividendos: {info.get('dividendRate', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Rendimento de dividendos: {info.get('dividendYield', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Data de ex-dividendo (formato Unix): {info.get('exDividendDate', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Taxa de dividendos anuais (últimos 12 meses): {info.get('trailingAnnualDividendRate', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Rendimento de dividendos anuais (últimos 12 meses): {info.get('trailingAnnualDividendYield', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Razão de pagamento de dividendos: {info.get('payoutRatio', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Yield médio de dividendos dos últimos 5 anos: {info.get('fiveYearAvgDividendYield', 'Não encontrado')}", ln = True, align = 'L')
pdf.ln(10)

# Índices financeiros

adiciona_topico("Índices Financeiros")
pdf.cell(200, 10, txt = f"Beta (Volatilidade): {info.get('beta', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"P/L Trailing (últimos 12 meses): {info.get('trailingPE', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"P/L Forward (próximos 12 meses): {info.get('forwardPE', 'Não encontrado')}", ln = True, align = 'L')
pdf.ln(10)

# Volume e liquidez

adiciona_topico("Volume e Liquidez")
pdf.cell(200, 10, txt = f"Volume médio: {info.get('averageVolume', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Volume médio dos últimos 10 dias: {info.get('averageVolume10days', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Volume médio diário dos últimos 10 dias: {info.get('averageDailyVolume10Day', 'Não encontrado')}", ln = True, align = 'L')
pdf.ln(10)

# Margens e valuation

adiciona_topico("Margens e Valuation")
pdf.cell(200, 10, txt = f"Margem de lucro: {info.get('profitMargins', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Preço/Venda (últimos 12 meses): {info.get('priceToSalesTrailing12Months', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Preço/Livro (valor contábil): {info.get('priceToBook', 'Não encontrado')}", ln = True, align = 'L')
pdf.ln(10)

# Valor contabil e de mercado

adiciona_topico("Valor Contábil e de Mercado")
pdf.cell(200, 10, txt = f"Valor de mercado da empresa: {info.get('marketCap', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Valor da empresa: {info.get('enterpriseValue', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Valor contábil por ação: {info.get('bookValue', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Preço/Valor Contábil (P/B): {info.get('priceToBook', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Valor da empresa dividido pela receita: {info.get('enterpriseToRevenue', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Valor da empresa dividido pelo EBITDA: {info.get('enterpriseToEbitda', 'Não encontrado')}", ln = True, align = 'L')
pdf.ln(10)

# Riscos

adiciona_topico("Riscos")
pdf.cell(200, 10, txt = f"Risco de Auditoria: {info.get('AuditRisk', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Risco da Diretoria: {info.get('BoardRisk', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Risco de Remuneração: {info.get('CompensationRisk', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Risco dos Direitos dos Acionistas: {info.get('ShareHolderRightsRisk', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Risco Geral: {info.get('OverallRisk', 'Não encontrado')}", ln = True, align = 'L')
pdf.ln(10)

# Abálise financeira

adiciona_topico("Análise Financeira")
pdf.cell(200, 10, txt = f"Número de opiniões de analistas: {info.get('numberOfAnalystOpinions', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Total de caixa da empresa: {info.get('totalCash', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Caixa por ação: {info.get('totalCashPerShare', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Lucro antes de juros, impostos, depreciação e amortização: {info.get('ebitda', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Total de dívida da empresa: {info.get('totalDebt', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Razão rápida (ativos circulantes/dívidas curtas): {info.get('quickRatio', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Razão corrente (ativos circulantes/dívidas curtas): {info.get('currentRatio', 'Não encontrado')}", ln = True, align = 'L')
pdf.ln(10)

# Desempenho financeiro

adiciona_topico("Desempenho Financeiro")
pdf.cell(200, 10, txt = f"Receita total da empresa: {info.get('totalRevenue', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Razão dívida/patrimônio: {info.get('debtToEquity', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Receita por ação: {info.get('revenuePerShare', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Retorno sobre ativos: {info.get('returnOnAssets', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10)

# Margens e fluxo de caixa

adiciona_topico("Margens e Fluxo de Caixa")
pdf.cell(200, 10, txt = f"Margem bruta: {info.get('grossMargins', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Margem EBITDA: {info.get('ebitdaMargins', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Margem operacional: {info.get('operatingMargins', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Fluxo de caixa livre: {info.get('freeCashflow', 'Não encontrado')}", ln = True, align = 'L')
pdf.cell(200, 10, txt = f"Fluxo de caixa operacional: {info.get('operatingCashflow', 'Não encontrado')}", ln = True, align = 'L')
pdf.ln(10)

# Crescimento financeiro

adiciona_topico("Crescimento Financeiro")
pdf.cell(200, 10, txt = f"Crescimento Financeiro: {round(info.get('revenueGrowth',0) \* 100, 2)}%", ln = True, align = 'L')
pdf.ln(10)

# Salvar PDF

nome*arquivo = f"relatorio*{info['symbol'].replace('.', '\_')}.pdf"
pdf.output(nome_arquivo)

```
