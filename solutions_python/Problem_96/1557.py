#!/usr/bin/python
#coding: utf-8
#autor: Nahu
#problem B

import sys

input = open(sys.argv[1], "r")
lineas = input.readlines()

for i in range(1, int(lineas[0]) + 1):
    enteros = lineas[i].split()
    enteros = map(int, enteros)
    googlers = enteros[0]
    sorpresas = enteros[1]
    p = enteros[2]
    puntos = enteros[3:]
    s0 = 0
    s12 = 0
    max = 0
    
    for point in puntos:
        div = point / 3
        mod = point % 3
        if div >= p or (div == p - 1 and mod != 0):
            s0 += 1
        elif (point > 0) and ((div == p - 1) or (div == p - 2 and mod == 2)):
            s12 += 1
    
    max = s0
    
    if sorpresas > s12:
        max += s12
    else:
        max += sorpresas
    
    salida = "Case #" + str(i) + ": " + str(max)
    print salida
