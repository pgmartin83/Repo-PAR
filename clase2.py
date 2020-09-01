"""
# LIST comprenhension
#metodo tradicional
lista = []
for numero in range(0, 11):
    if numero % 2 == 0:
        lista.append(numero ** 2)
print(lista)

#list comprenhension
lista_c = [numero ** 2 for numero in range(0, 11) if numero % 2 == 0]
print(lista_c)
"""

"""
#LAMBDA
#tradicional
def doblar(numero):
    resultado = numero * 2
    return resultado

resultado = doblar(2)
print(resultado)

#simplificado
def doblar2(numero):
    return numero * 2

print(doblar2(2))

#simplificado LAMBDA
doblar3 = lambda numero: numero * 2

print(doblar3(2))
"""
"""
#filter()
def multiple(numeros):
    if numeros % 5 == 0:
        return True

numeros  = [2, 5, 10, 23, 50, 33]

resultado = list( filter(multiple, numeros) )

print(resultado)

#filter() + LAMBDA

resultado2 = list( filter(lambda numero: numero % 5 == 0, numeros) )

print(resultado2)
"""
"""
#map()
numeros  = [2, 5, 10, 23, 50, 33]

def doblar(numero):
	return numero * 2

print( list(map(doblar, numeros)) )

#map() + LAMBDA
print(list(map(lambda x: x*2, numeros)))
"""

#recursividad
#Ejemplo factorial
def factorial(numero):
    if numero == 0:
        return 1
    else:
        print(f"soy el {numero}")
        #recur = factorial(numero -1)
        #da = recur * numero
        #return da
        return factorial(numero -1) * numero

print(factorial(5))

#Ejemplo fibonacci
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
#1 1 2 3 5 8 13 21 34 55 89 144 233
print(fibonacci(10))
