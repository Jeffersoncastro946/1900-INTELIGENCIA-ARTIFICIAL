# Ejercicio 1: Análisis de Ventas
# Utilice el archivo ventas.csv para responder lo siguiente:
# Cargue los datos en un DataFrame.
# Calcule la cantidad total de productos vendidos por categoría.
# Determine cuál es el producto con el mayor total de ventas.
# Encuentre el precio promedio de los productos vendidos.

import pandas as pd

# Cargar los datos desde el CSV
df = pd.read_csv("ventas.csv")

# Agregar columna de total por cada venta
df["Total_Venta"] = df["Cantidad"] * df["Precio_Unitario"]

# 1. Cantidad total de productos vendidos por categoría
total_por_producto = df.groupby("Producto")["Cantidad"].sum()
print("Cantidad total por producto:")
print(total_por_producto)

# 2. Producto con el mayor total de ventas (en dinero)
ventas_totales_por_producto = df.groupby("Producto")["Total_Venta"].sum()
producto_mayor_ventas = ventas_totales_por_producto.idxmax()
monto_mayor_ventas = ventas_totales_por_producto.max()

print(
    f"\nProducto con mayor total de ventas: {producto_mayor_ventas} (L. {monto_mayor_ventas:.2f})")

# 3. Precio promedio de los productos vendidos (ponderado por cantidad)
precio_promedio_ponderado = (
    df["Precio_Unitario"] * df["Cantidad"]).sum() / df["Cantidad"].sum()
print(
    f"\nPrecio promedio ponderado de los productos vendidos: L. {precio_promedio_ponderado:.2f}")
