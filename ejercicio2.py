# Ejercicio 2
from random import randint

# Entrada de datos
num1 = int(input("Ingrese límite inferior: "))
num2 = int(input("Ingrese límite superior: "))

# Generar número aleatorio
numero = randint(num1, num2)

# Ajustar a número par
if numero % 2 != 0:
    if numero + 1 <= num2:
        numero = numero + 1
    else:
        numero = numero - 1

# Juego de 3 intentos
intento1 = int(input("Intente adivinar: "))
if intento1 == numero:
    print("Felicitaciones, pudiste adivinar.")
else:
    if intento1 < numero:
        print("El número es mayor.")
    else:
        print("El número es menor.")

    intento2 = int(input("Intente de nuevo: "))
    if intento2 == numero:
        print("Felicitaciones, pudiste adivinar.")
    else:
        if intento2 < numero:
            print("El número es mayor.")
        else:
            print("El número es menor.")

# cálculo de distancias
    dif1 = intento1 - numero
    if dif1 < 0:
        dif1 = -dif1

    dif2 = intento2 - numero
    if dif2 < 0:
        dif2 = -dif2

    if dif1 < dif2:
        print("Te daré una pista: El número está más cerca de", intento1)
    else:
        print("Te daré una pista: El número está más cerca de", intento2)

    intento3 = int(input("Intente la última vez: "))
    if intento3 == numero:
        print("Felicitaciones, pudiste adivinar.")
    else:
        print("Perdiste. El número era:", numero)
