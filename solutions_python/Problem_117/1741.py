#!/usr/bin/python

import sys

def checking(columnas_buenas, array):
    for i in range(alto):
        fila = array[i*ancho:i*ancho+ancho]
        if len(set(fila)) == 1:
            continue
        maxi = max(fila)
        for j in range(ancho):
            if fila[j] != maxi and not (j in columnas_buenas):
                return False;

    return True

with open(sys.argv[1]) as f:
    lines = f.readlines();

# Quito primera linea que suele ser el numero de casos que hay
# y se puede deducir del numero de lineas del fichero restantes
cases = int(lines.pop(0))

n_case = 0
for asdf in range(cases):
    n_case += 1
    line = lines.pop(0)
    alto, ancho = [int(c) for c in line.split(' ')]
    #if alto == 1 or ancho == 1:
    #    print("Case #"+str(n_case)+": YES")
    #    continue
    array = []
    for i in range(alto):
        array += [int(c) for c in lines.pop(0).split(' ')]

    if (len(set(array)) == 1):
        print("Case #"+str(n_case)+": YES")
        continue

    columnas_buenas = []
    for i in range(ancho):
        columna = []
        for j in range(i, alto*ancho, ancho):
            columna.append(array[j])
        if len(set(columna)) == 1:
            columnas_buenas.append(i)

    if checking(columnas_buenas, array):
        print("Case #"+str(n_case)+": YES")
    else:
        print("Case #"+str(n_case)+": NO")
