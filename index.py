import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

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
data.drop(['Rank', 'Name', 'Year', 'Other_Sales', 'Global_Sales'], axis=1, inplace=True)

# Descobrir quais colunas possuem valores nulos

# Com isso, descobrimos que a coluna 'Publisher' possui 58 valores nulos. O restante, possuem 0 valores nulos
# Consideramos que os valores 0 nas vendas tem um significado para a análise, portanto não iremos apagar nem substituir esses valores

# Junção da tabela de vendas da América do Norte e Europa, para criar uma nova variável alvo (OCIDENTE)
data["West_Sales"] = data["NA_Sales"] + data["EU_Sales"]

# Mudança na nomenclatura da variável alvo para vendas do Japão, para criar uma nova variável alvo (ORIENTE)
data["East_Sales"] = data["JP_Sales"]

alvos = ["West_Sales", "East_Sales"]
colunas_vendas = ["NA_Sales", "EU_Sales", "JP_Sales"]

# Coluna da variável alvo
y = data[alvos]
X = data.drop(columns=colunas_vendas + alvos)

# Selecionar colunas categóricas 
colunas_categoricas = X.select_dtypes(include=['object']).columns.tolist()

# Selecionar colunas numéricas
colunas_numericas = X.select_dtypes(include=['int64', 'float64']).columns.tolist()

# Pré-processamento das colunas categóricas e das colunas numéricas
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), colunas_categoricas),
        ('imputer', SimpleImputer(strategy='constant', fill_value='Unknown')),
        ('num', StandardScaler(), colunas_numericas)
    ]
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train_proc = preprocessor.fit_transform(X_train)   # aprende só no treino
X_test_proc = preprocessor.transform(X_test)          # só aplica no teste