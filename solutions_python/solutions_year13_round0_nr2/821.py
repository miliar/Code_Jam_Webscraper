##numpy free available in http://www.numpy.org/
from numpy import *

entrada = open("B-large.in", "r")
salida = open("output.txt", "w")
casos = int(entrada.readline())

for caso in range(casos):
    n, m = map(int,entrada.readline().split())
    lista = []

    for linea in range(n):
        lista =  lista + map(int,entrada.readline().strip().split())

    elementos = list(set(lista))
    elementos.sort()
    tabla = array(lista).reshape(n,m)

    for e in elementos:
        for i in range(n):
            for j in range(m):
                if tabla[i,j] == e:
                    if set(tabla[i,:]) == set([e]):
                        tabla[i,:] *= 0
                    elif set(tabla[:,j]) == set([e]): 
                        tabla[:,j] *= 0
                    elif set(tabla[i,:]) == set([e,0]):
                        tabla[i,:] *= 0
                    elif set(tabla[:,j]) == set([e,0]):
                        tabla[:,j] *= 0
                        
    if tabla.sum() == 0:
        salida.write("Case #"+str(caso+1)+": YES\n")
    else:
        salida.write("Case #"+str(caso+1)+": NO\n")

entrada.close()
salida.close()
