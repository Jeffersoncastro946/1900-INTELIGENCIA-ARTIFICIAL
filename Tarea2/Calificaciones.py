# Ejercicio 3: Estadísticas de Calificaciones
# Utilice el archivo calificaciones.csv para analizar el rendimiento de los estudiantes:
# Cargue el dataset y muestre las primeras filas.
# Calcule el promedio de calificaciones por materia.
# Identifique el estudiante con el promedio más alto.
# Agrupa las calificaciones por estudiante y calcule el promedio de cada uno.
# Identifique cuántos estudiantes tienen un promedio superior a 85.
# Encuentre la materia con la mayor cantidad de calificaciones registradas.
# Muestre los 5 estudiantes con el promedio más bajo.

import pandas as pd

# Cargar el dataset
df = pd.read_csv("calificaciones.csv")

# Mostrar las primeras filas
print("Primeras filas del dataset:")
print(df.head())

# 1. Calcular el promedio de calificaciones por materia
promedio_por_materia = df.groupby(
    "Materia")["Calificación"].mean().sort_values(ascending=False)
print("\nPromedio por materia:")
print(promedio_por_materia)

# 2. Agrupar por estudiante y calcular su promedio
promedio_por_estudiante = df.groupby("Estudiante")["Calificación"].mean()

# 3. Estudiante con el promedio más alto
mejor_estudiante = promedio_por_estudiante.idxmax()
mejor_promedio = promedio_por_estudiante.max()
print(
    f"\nEstudiante con el mejor promedio: {mejor_estudiante} ({mejor_promedio:.2f})")

# 4. Cuántos estudiantes tienen un promedio mayor a 85
estudiantes_sobresalientes = (promedio_por_estudiante > 85).sum()
print(
    f"\nCantidad de estudiantes con promedio mayor a 85: {estudiantes_sobresalientes}")

# 5. Materia con más calificaciones registradas
materia_mas_comun = df["Materia"].value_counts().idxmax()
cantidad_registros = df["Materia"].value_counts().max()
print(
    f"\nMateria con más calificaciones registradas: {materia_mas_comun} ({cantidad_registros} registros)")

# 6. Los 5 estudiantes con el promedio más bajo
estudiantes_peor_promedio = promedio_por_estudiante.sort_values().head(5)
print("\n5 estudiantes con el promedio más bajo:")
print(estudiantes_peor_promedio)
