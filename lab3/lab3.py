import pandas as pd
import matplotlib.pyplot as plt

# Carga el archivo csv en un DataFrame
data = pd.read_csv('./Womens Clothing E-Commerce Reviews.csv')

print(data.head())

# Muestra un resumen de la estructura del DataFrame
print(data.info())

# Muestra los nombres de las columnas del DataFrame
print(data.columns)

# Muestra los tipos de datos de cada columna del DataFrame
print(data.dtypes)

# Muestra un resumen estadístico de las columnas numéricas del DataFrame
print(data.describe())

# Muestra el número de filas y columnas del DataFrame
print(data.shape)


# Crea un nuevo DataFrame con las columnas deseadas
new_data = data.loc[:, ['Age', 'Rating', 'Recommended IND', 'Positive Feedback Count', 'Division Name', 'Department Name', 'Class Name']]

# Muestra el nuevo DataFrame
print(new_data)

#Las variables categorías son aquellas que toman un número limitado de valores discretos y representan una categoría o etiqueta. 
#en este conjunto de datos son: Division Name, Department Name y Class Name.

# Muestra los valores únicos en la columna "Rating"
unique_ratings = data['Rating'].unique()
print("Valores únicos en la columna 'Rating':", unique_ratings)

# Muestra los valores únicos en la columna "Recommended IND"
unique_recommended = data['Recommended IND'].unique()
print("Valores únicos en la columna 'Recommended IND':", unique_recommended)

# Muestra los valores únicos en la columna "Positive Feedback Count"
unique_positive_feedback = data['Positive Feedback Count'].unique()
print("Valores únicos en la columna 'Positive Feedback Count':", unique_positive_feedback)

# Muestra la cantidad de valores nulos por columna
null_count = data.isnull().sum()
print("Cantidad de valores nulos por columna:\n", null_count)

# Muestra las columnas que contienen valores nulos
null_columns = data.columns[data.isnull().any()]
print("Columnas que contienen valores nulos:\n", null_columns)

#Renombrar columnas en espanol
data = data.rename(columns={0: 'ID', 'Clothing ID': 'ID de ropa', 'Age': 'Edad', 'Title': 'Título', 'Review Text': 'Texto de la reseña', 'Rating': 'Calificación', 'Recommended IND': 'Recomendado', 
   'Positive Feedback Count': 'Cantidad de comentarios positivos', 'Division Name': 'Nombre de la división', 'Department Name': 'Nombre del departamento', 'Class Name': 'Nombre de la clase'})
print(data)

#Columnas categoricas
categorical_div = 'Division Name'
categorical_class = 'Division Name'
categorical_dept = 'Division Name'

# crear un gráfico boxplot para cada valor único en la columna categórica
for value in data[categorical_div].unique():
   subset = data[data[categorical_div] == value]
   plt.boxplot(subset['Rating'], labels=[value])
   plt.title(value)
   plt.show()
    
for value in data[categorical_class].unique():
   subset = data[data[categorical_class] == value]
   plt.boxplot(subset['Rating'], labels=[value])
   plt.title(value)
   plt.show()

for value in data[categorical_dept].unique():
   subset = data[data[categorical_dept] == value]
   plt.boxplot(subset['Rating'], labels=[value])
   plt.title(value)
   plt.show()


plt.figure()
for elemento in data[categorical_div].unique():
    plt.hist(data[data[categorical_div]==elemento]['Age'], alpha=0.5, label=elemento)
plt.legend(loc='upper right')
plt.title("Histogramas de Edad para cada Elemento de " + categorical_div)
plt.xlabel("Age")
plt.ylabel("Frecuencia")
plt.show()

# Generar histogramas de la edad para cada elemento de la variable categórica B
plt.figure()
for elemento in data[categorical_class].unique():
    plt.hist(data[data[categorical_class]==elemento]['Age'], alpha=0.5, label=elemento)
plt.legend(loc='upper right')
plt.title("Histogramas de Edad para cada Elemento de " + categorical_class)
plt.xlabel("Age")
plt.ylabel("Frecuencia")
plt.show()

# Generar histogramas de la edad para cada elemento de la variable categórica C
plt.figure()
for elemento in data[categorical_dept].unique():
    plt.hist(data[data[categorical_dept]==elemento]['Age'], alpha=0.5, label=elemento)
plt.legend(loc='upper right')
plt.title("Histogramas de Edad para cada Elemento de " + categorical_dept)
plt.xlabel("Age")
plt.ylabel("Frecuencia")
plt.show()


# Agrupar por Division Name y convertir el resultado en un dataframe
division_grouped = data.groupby("Division Name").count().reset_index()
division_grouped = division_grouped[["Division Name", "Clothing ID"]]
division_grouped = division_grouped.rename(columns={"Clothing ID": "Cantidad"})
print(division_grouped)

# Agrupar por Department Name y convertir el resultado en un dataframe
department_grouped = data.groupby("Department Name").count().reset_index()
department_grouped = department_grouped[["Department Name", "Clothing ID"]]
department_grouped = department_grouped.rename(columns={"Clothing ID": "Cantidad"})
print(department_grouped)

# Agrupar por Class Name y convertir el resultado en un dataframe
class_grouped = data.groupby("Class Name").count().reset_index()
class_grouped = class_grouped[["Class Name", "Clothing ID"]]
class_grouped = class_grouped.rename(columns={"Clothing ID": "Cantidad"})
print(class_grouped)

# Gráfico de Pie para Division Name
division_grouped.plot(kind="pie", y="Cantidad", labels=division_grouped["Division Name"], autopct="%1.1f%%", startangle=90)
plt.title("Distribución de Division Name")
plt.ylabel("")
plt.show()

# Gráfico de Barras para Division Name
division_grouped.plot(kind="bar", x="Division Name", y="Cantidad", color="blue")
plt.title("Cantidad de registros por Division Name")
plt.xlabel("Division Name")
plt.ylabel("Cantidad")
plt.show()

# Gráfico de Pie para Department Name
department_grouped.plot(kind="pie", y="Cantidad", labels=department_grouped["Department Name"], autopct="%1.1f%%", startangle=90)
plt.title("Distribución de Department Name")
plt.ylabel("")
plt.show()

# Gráfico de Barras para Department Name
department_grouped.plot(kind="bar", x="Department Name", y="Cantidad", color="blue")
plt.title("Cantidad de registros por Department Name")
plt.xlabel("Department Name")
plt.ylabel("Cantidad")
plt.show()

# Gráfico de Pie para Class Name
class_grouped.plot(kind="pie", y="Cantidad", labels=class_grouped["Class Name"], autopct="%1.1f%%", startangle=90)
plt.title("Distribución de Class Name")
plt.ylabel("")
plt.show()

# Gráfico de Barras para Class Name
class_grouped.plot(kind="bar", x="Class Name", y="Cantidad", color="blue")
plt.title("Cantidad de registros por Class Name")
plt.xlabel("Class Name")
plt.ylabel("Cantidad")
plt.show()


#Calcular promedio de edad para nombre de division
promedio_edad_division = data.groupby("Division Name")["Age"].mean()
print(promedio_edad_division)

#Calcular promedio de edad para nombre de departamento
promedio_edad_department = data.groupby("Department Name")["Age"].mean()
print(promedio_edad_department)

#Calcular promedio de edad para nombre de clase
promedio_edad_class = data.groupby("Class Name")["Age"].mean()
print(promedio_edad_class)


