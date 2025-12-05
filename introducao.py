""" nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print(f"Olá, {nome}! Você tem {idade} anos.") 

def sacar(valor):
    saldo = 1000
    if valor > saldo:
        print("Saldo insuficiente para saque.")
    else:
        saldo -= valor
        print(f"Saque de R${valor} realizado com sucesso. Saldo restante: R${saldo}.")

sacar(500) """
# Introdução à Análise de Dados com Pandas


import pandas as pd
import matplotlib.pyplot as plt

# 1. Criando nossos dados (simulando um arquivo Excel/CSV)
dados = {
    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Cadeira Gamer'],
    'Vendas_Unidades': [10, 150, 80, 45, 20],
    'Preco_Unitario': [3500, 50, 150, 800, 1200]
}

# 2. Transformando em um DataFrame (a tabela inteligente do Pandas)
df = pd.DataFrame(dados)

# 3. Criando uma nova informação: Faturamento por produto
# (Multiplicamos a coluna de unidades pela coluna de preço)
df['Faturamento_Total'] = df['Vendas_Unidades'] * df['Preco_Unitario']

# 4. Extraindo Insights (A "Ciência" dos dados)
produto_campeao = df.loc[df['Faturamento_Total'].idxmax()]
faturamento_total_loja = df['Faturamento_Total'].sum()

print("--- 📊 Relatório de Vendas ---")
print(f"Faturamento Total da Loja: R$ {faturamento_total_loja:,.2f}")
print(f"Produto que mais gerou dinheiro: {produto_campeao['Produto']} (R$ {produto_campeao['Faturamento_Total']:,.2f})")
print("\nVeja a tabela completa:")
print(df)

# 5. Visualização (O Gráfico)
# Vamos ver quem vendeu mais unidades?
plt.figure(figsize=(8, 5))
plt.bar(df['Produto'], df['Vendas_Unidades'], color='skyblue')
plt.title('Quantidade de Produtos Vendidos')
plt.xlabel('Produtos')
plt.ylabel('Unidades Vendidas')
plt.show()