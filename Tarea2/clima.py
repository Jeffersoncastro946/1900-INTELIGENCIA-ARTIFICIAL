# ️ Ejercicio 2: Análisis del Clima
# -Utilice el archivo clima.csv para analizar los datos climáticos:
# -Cargue el dataset y conviértelo en un DataFrame.
# -Calcule la temperatura promedio de cada ciudad.
# -Determine el registro con la temperatura más alta y el más bajo en el dataset.
# -Identifique qué ciudad tuvo la temperatura más alta y cuál la más baja en todo el dataset.
# -Encuentre cuántos registros tienen una temperatura mayor a 30°C.
# -Cuenta cuántos días en total hay registrados por cada ciudad.
import pandas as pd

# Cargue el dataset y conviértelo en un DataFrame.
df_clima = pd.read_csv("clima.csv")

# Calcule la temperatura promedio de cada ciudad.
temperatura_promedio_por_ciudad = df_clima.groupby("Ciudad")[
    "Temperatura"].mean()
print("Temperatura promedio por ciudad:")
print(temperatura_promedio_por_ciudad)

# Determine el registro con la temperatura más alta y el más bajo en el dataset
temperatura_maxima = df_clima["Temperatura"].max()
temperatura_minima = df_clima["Temperatura"].min()
print(f"\nla temperatura más alta: {temperatura_maxima}")
print(f"la temperatura más baja: {temperatura_minima}")
print(" ")
# Identifique qué ciudad tuvo la temperatura más alta y cuál la más baja en todo el dataset.
indice = df_clima.Temperatura.idxmax()

print(
    f"la temperaturea mas alta la tuvo: {df_clima.loc[indice].Ciudad} con {df_clima.loc[indice].Temperatura} ")
print(" ")
indice = df_clima.Temperatura.idxmin()
print(
    f"la temperaturea mas baja la tuvo: {df_clima.loc[indice].Ciudad} con {df_clima.loc[indice].Temperatura}")

# Encuentre cuántos registros tienen una temperatura mayor a 30°C.
registros_temperatura_mayor_30 = df_clima[df_clima["Temperatura"] > 30]
cantidad_registros_mayor_30 = len(registros_temperatura_mayor_30)
print(
    f"\nCantidad de registros con temperatura mayor a 30°C: {cantidad_registros_mayor_30}")

# Cuenta cuántos días en total hay registrados por cada ciudad.
dias_por_ciudad = df_clima.groupby("Ciudad")["Fecha"].count()
print("\nCantidad de días registrados por cada ciudad:")
print(dias_por_ciudad)
