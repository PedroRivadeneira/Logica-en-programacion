# Mensaje inicial para el usuario:
# Explica qué debe hacer: pensar un número entre 1 y 100.

print("Piensa en un número entre 1 y 100, y yo intentaré adivinarlo.")

# Pausa para que el usuario esté listo antes de continuar.
input("Presiona Enter cuando estés listo...")

# Inicialización de variables:
# 'bajo'  = límite menor del rango de búsqueda (empieza en 1)
# 'alto'  = límite mayor del rango de búsqueda (empieza en 100)
# 'intentos' = contador de intentos usados para adivinar

bajo = 1
alto = 100
intentos = 0

# Bucle principal:
# Se repite indefinidamente hasta encontrar el número

while True:

    # Cálculo del punto medio entre 'bajo' y 'alto'
   
    intento = (bajo + alto) // 2

     # Incrementamos el contador de intentos.
    intentos += 1

    # Solicitamos al usuario que indique si el número pensado es mayor, menor o si está correcto.
    # .lower() convierte la respuesta a minúsculas para evitar errores.

    respuesta = input(f"¿Tu número es {intento}? (responde 'mayor', 'menor' o 'correcto'): ").lower()

    if respuesta == 'correcto':
        print(f"¡Genial! Adiviné tu número en {intentos} intento(s).")
        break
    elif respuesta == 'mayor':
        bajo = intento + 1
    elif respuesta == 'menor':
        alto = intento - 1
    else:
        print("Por favor, responde solo con 'mayor', 'menor' o 'correcto'.")


