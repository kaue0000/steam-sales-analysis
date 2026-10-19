import pandas as pd

data = pd.read_csv('./vgsales.csv')
# Visualização das primeiras linhas do dataset
print("-"*20 + "Primeiras linhas do dataset" + "-"*20)
print(data.head())

# Visualização das últimas linhas do dataset
print("-"*20 + "Últimas linhas do dataset" + "-"*20)
print(data.tail())

print("-"*20 + "Formato do dataset" + "-"*20)
print(data.shape)
# Com a execução desse método temos a certeza de que o dataset se encaixa nos requisitos, que seria ter 1000 instâncias.