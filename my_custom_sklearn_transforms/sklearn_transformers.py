from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

 rm_columns = DropColumns(
    columns=["NOME", "INGLES", "H_AULA_PRES", "TAREFAS_ONLINE", "FALTAS"]  # Essa transformação recebe como parâmetro uma lista com os nomes das colunas indesejadas
)

print(rm_columns)   


# Visualizando as colunas do dataset original
print("Colunas do dataset original: \n")
print(df_data_1.columns)

# Aplicando a transformação ``DropColumns`` ao conjunto de dados base
rm_columns.fit(X=df_data_1)

# Reconstruindo um DataFrame Pandas com o resultado da transformação
df_data_2 = pd.DataFrame.from_records(
    data=rm_columns.transform(
        X=df_data_1
    )
)


# Visualizando as colunas do dataset transformado
print("Colunas do dataset após a transformação ``DropColumns``: \n")
print(df_data_2.columns)


import pandas as pd

from sklearn.impute import SimpleImputer

si = SimpleImputer(missing_values=np.nan, strategy='constant', fill_value=0, verbose=0, copy=True)

# Aplicamos o SimpleImputer ``si`` ao conjunto de dados df_data_2 (resultado da primeira transformação)
    
si.fit(X=df_data_2)


# Visualizando os dados faltantes do dataset após a primeira transformação (df_data_2)
print("Valores nulos antes da transformação SimpleImputer: \n\n{}\n".format(df_data_2.isnull().sum(axis = 0)))


# Reconstrução de um novo DataFrame Pandas com o conjunto imputado (df_data_3)

df_data_3=pd.DataFrame.from_records(
    data=si.transform(
        X=df_data_2)  # o resultado SimpleImputer.transform(<<pandas dataframe>>) é lista de listas
       # as colunas originais devem ser conservadas nessa transformação
)   
     
print(df_data_3)


# Visualizando os dados faltantes do dataset após a segunda transformação (SimpleImputer) (df_data_3)
print("Valores nulos no dataset após a transformação SimpleImputer: \n\n{}\n".format(df_data_3.isnull().sum(axis = 0)))

df_data_3.head()



