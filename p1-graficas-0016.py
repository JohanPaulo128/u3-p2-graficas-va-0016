import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Definición de la lista de planetas (Nombre, Distancia al Sol en Mkm, Tiene anillos, Año)
mer = ['Mercurio', 57.9, False, 1631]
ven = ['Venus', 108.2, False, 1610]
tie = ['Tierra', 149.6, False, 0]
mar = ['Marte', 227.9, False, 1610]
jup = ['Júpiter', 778.5, True, 1610]

lista_planetas = [mer, ven, tie, mar, jup]

# Crear el DataFrame con columnas adaptadas a los nuevos datos
df_planetas = pd.DataFrame(lista_planetas, columns=["Nombre", "Distancia", "Tiene_Anillos", "Año"])
print(df_planetas)

# Guardar la tabla en un archivo CSV
df_planetas.to_csv("planetas.csv", index=False)

# 1. Gráfica de líneas
plt.plot(df_planetas["Nombre"], df_planetas["Distancia"])
plt.title("Distancia de los planetas al Sol NC 0016")
plt.xlabel("Nombre del planeta")
plt.ylabel("Distancia (Mkm)")
plt.show()

# 2. Gráfica de dispersión (Scatter)
plt.scatter(df_planetas["Nombre"], df_planetas["Distancia"])
plt.title("Dispersión de distancias al Sol NC 0016")
plt.xlabel("Nombre del planeta")
plt.ylabel("Distancia (Mkm)")
plt.show()

# 3. Gráfica de barras
plt.bar(df_planetas["Nombre"], df_planetas["Distancia"])
plt.title("Distancia al Sol por planeta NC 0016")
plt.xlabel("Planeta")
plt.ylabel("Distancia (Mkm)")
plt.show()

# 4. Ordenar la gráfica de barras de manera descendente
df_planetas_ordenar = df_planetas.sort_values("Distancia", ascending=False)
plt.bar(df_planetas_ordenar["Nombre"], df_planetas_ordenar["Distancia"])
plt.title("Planetas ordenados por distancia (Mayor a menor) NC 0016")
plt.xlabel("Planeta")
plt.ylabel("Distancia (Mkm)")
plt.show()

# 5. Coloreando la gráfica de barras (5 colores para los 5 planetas)
plt.bar(df_planetas_ordenar["Nombre"], df_planetas_ordenar["Distancia"], 
        color=["b", "g", "c", "m", "y"])
plt.title("Planetas ordenados por distancia (Coloreados) NC 0016")
plt.xlabel("Planeta")
plt.ylabel("Distancia (Mkm)")
plt.show()

# 6. Gráfica de pastel
plt.pie(df_planetas["Distancia"], labels=df_planetas["Nombre"], autopct='%1.1f%%')
plt.title("Proporción de distancia al Sol NC 0016")
plt.show()