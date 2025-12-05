# Relatório de Vendas com Python

Este repositório contém um script em **Python** que simula dados de vendas de uma loja, realiza cálculos de faturamento e gera insights, além de criar uma visualização gráfica das unidades vendidas por produto.

---

## Funcionalidades
- Criação de dados simulados (como se fossem importados de um Excel/CSV).
- Transformação dos dados em um **DataFrame** usando **Pandas**.
- Cálculo automático do **faturamento total por produto**.
- Identificação do produto campeão em faturamento.
- Exibição de relatório no console.
- Geração de gráfico de barras com **Matplotlib** mostrando a quantidade de produtos vendidos.

---

## Estrutura do Script
1. **Criação dos dados**: Produtos, unidades vendidas e preços unitários.  
2. **DataFrame**: Organização dos dados em tabela inteligente.  
3. **Cálculo de faturamento**: Multiplicação de unidades por preço.  
4. **Insights**: Produto campeão e faturamento total da loja.  
5. **Visualização**: Gráfico de barras das unidades vendidas.  

---

## Tecnologias Utilizadas
- [Python 3](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)

---

## Exemplo de Saída no Console

![Saida do console](https://github.com/robsonosbor/python-analise-vendas/blob/main/saida_console.png)


---

## Gráfico Gerado
O script gera um gráfico de barras mostrando a quantidade de produtos vendidos:

- **Eixo X**: Produtos  
- **Eixo Y**: Unidades vendidas  
- **Cor**: Azul claro (skyblue)  

![Gráfico](https://github.com/robsonosbor/python-analise-vendas/blob/main/grafico.png)

## Observações
- Este projeto é apenas um exemplo didático para demonstrar como usar Pandas e Matplotlib em análises simples de dados.
- Pode ser facilmente adaptado para ler dados reais de arquivos CSV ou Excel.
