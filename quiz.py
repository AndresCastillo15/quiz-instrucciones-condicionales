# Quiz instrucciones condicionales
"""Dados tres números a, b y c, correspondientes a la longitud de los lados de una figura geométrica, determinar si pueden formar los lados de un triángulo."""

print("╔═════════════════════════════╗")
print("----- VERIFICAR TRIÁNGULO ----")
print("╚═════════════════════════════╝")

# input
print("╔═══════════════════════════════════╗")
lado1 = float(input("Elige el primer dígito (Lado 1): "))
lado2 = float(input("Elige el segundo dígito (Lado 2): "))
lado3 = float(input("Elige el tercer dígito (Lado 3): "))
print("╚═══════════════════════════════════╝")
# processing
if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    respuesta = "Las longitudes deben ser mayores que cero."
else:
    if lado1 + lado2 > lado3:
        if lado1 + lado3 > lado2:
            if lado2 + lado3 > lado1:
                respuesta = "¡Sí, estos lados pueden formar un triángulo!"
            else:
                respuesta = "No, estos lados no pueden formar un triángulo."
        else:
            respuesta = "No, estos lados no pueden formar un triángulo."
    else:
        respuesta = "No, estos lados no pueden formar un triángulo."

# Output
print("╔════════════════════════════════════╗")
print("Resultado: " + respuesta)
print(f"Lados ingresados: {lado1}, {lado2}, {lado3}")
print("╚════════════════════════════════════╝")
