#Ejercicio 3
# Crear un programa que imprima por pantalla todos los números del 0 al 100 que sean divisibles por 3.
"""
def ejercicio3():
    for number in range(0, 101):
        if number%3 == 0:
            print(number)

ejercicio3()
"""
# Ejercicio 5
# Crear un programa que pida al usuario 10 números enteros, los almacene en una lista, ordene los números dentro de la lista y luego imprima por pantalla la lista completa y ordenada.
"""
def ejercicio5():
    userValueList = []
    for number in range(10):
        userValueList.append(int(input(f"Ingrese un número entero {number}: ")))

    userValueList.sort()
    print(userValueList)

ejercicio5()
"""
# Ejercicio 6
# Crear un programa que le pida al usuario dos números enteros y luego: si el primero es mayor que el segundo, retorne 1, si el primero es menor que el segundo retorne -1 y si ambos números son iguales retorne 0.
"""
def ejercicio6(number1, number2):
    if number1 > number2:
        return 1
    elif number1 < number2:
        return -1
    else:
        return 0

userInput1 = int(input("Ingrese un número entero: "))
userInput2 = int(input("Ingrese un número entero: "))

resultado = (ejercicio6(userInput1, userInput2))
print(resultado)
"""
# Ejercicio 11
# Crear un programa que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras están separadas por uno o más espacios. También podría haber espacios al principio o al final del string pasado por parámetro.

def ejercicio11(userInput):
    wordList = userInput.split()
    return len(wordList[-1])

print(ejercicio11("Bienvenidos a paradigmas de programación"))
