import pandas as pd

# Leer los datos
datos = pd.read_csv("ventas.csv")

# Calcular el importe de cada venta
datos["total"] = datos["cantidad"] * datos["precio"]

# Mostrar resultados
print("REGISTRO DE VENTAS")
print(datos)

print("\nTOTAL DE VENTAS:")
print(datos["total"].sum())

print("\nPRODUCTO MAS VENDIDO:")
print(datos.loc[datos["cantidad"].idxmax(), "producto"])
