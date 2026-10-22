import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

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


# Apagar colunas desnecessárias para a análise
data.drop(['Rank', 'Name', 'Year'], axis=1, inplace=True)

# Descobrir quais colunas possuem valores nulos

# Com isso, descobrimos que a coluna 'Publisher' possui 58 valores nulos. O restante, possuem 0 valores nulos
# Consideramos que os valores 0 nas vendas tem um significado para a análise, portanto não iremos apagar nem substituir esses valores

# Coluna da variável alvo - Teste
y = data[["JP_Sales", "US_Sales", "EU_Sales"]]
X = data.drop(columns=[y])

# Selecionar colunas categóricas 
colunas_categoricas = data.select_dtypes(include=['object']).columns.tolist()

# Selecionar colunas numéricas
colunas_numericas = data.select_dtypes(include=['int64', 'float64']).columns.tolist()

# Pré-processamento das colunas categóricas e das colunas numéricas
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), colunas_categoricas),
        ('num', StandardScaler(), colunas_numericas)
    ]
)