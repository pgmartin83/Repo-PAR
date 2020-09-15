#def cochesYmotos(vehiculos, ruedas):
#    coche = ruedas / 2 - vehiculos
#    moto = vehiculos - coche
#    print(f"cantidad de coches {coche} y de motos {moto} y de vehiculos {vehiculos}")

#    if (int(coche) + int(moto) == vehiculos):
#        print(f"ruedas de autos: {int(coche) * 4} + ruedas de motos: {int(moto) * 2} = total de ruedas: {ruedas}")
#        return coche, moto

#cochesYmotos(6, 20)

#Ordenar listas
#Unidad 19 aprendiendo a programar en python

#Ordenamiento simple
#O N2
listaEntrada = [3,2,-1,5,0,2]

def orden_seleccion(lista):
    ultimaPosicion = len(lista) - 1

    while ultimaPosicion > 0:
        mayorElemento = buscar_max(lista, 0 , ultimaPosicion)
        lista[mayorElemento], lista[ultimaPosicion] = lista[ultimaPosicion], lista[mayorElemento]
        print(f"DEBUG: posición mayor {mayorElemento}, última posición {ultimaPosicion}, {lista}")
        ultimaPosicion = ultimaPosicion - 1

def buscar_max(lista, inicio, fin):
    pos_MAX = inicio
    for i in range(inicio + 1, fin + 1):
        #print(f"posicion i {i}, inicio {inicio}, fin {fin}")
        if lista[i] > lista[pos_MAX]:
            print(f"Posición i {lista[i]} es mayor que {lista[pos_MAX]}")
            pos_MAX = i

    return pos_MAX

print(listaEntrada)
print(orden_seleccion(listaEntrada))

#Ordenamiento por inserción
listaEntrada = [3,2,-1,5,0,2]

def ord_insercion(lista):
    for i in range(len(lista) - 1):
        if lista[i+1] < lista[i]:
            reubicar(lista, i+1)
        print("DEBUG: ", lista)

def reubicar(lista, pos):
    valorPos = lista[pos]
    posOrig = pos
    while posOrig > 0 and valorPos < lista[posOrig - 1]:
        lista[posOrig] = lista[posOrig - 1]
        posOrig -= 1

    lista[posOrig] = valorPos

ord_insercion(listaEntrada)

#Ejercicio 19.4.1. Implementar una función que reciba una lista y devuelva otra lista con los mismos elementos que la primera,
#ordenados de mayor a menor mediante el método de inserción.
