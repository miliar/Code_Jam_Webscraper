import sys
import os


arquivo = open('a_small.in','r')
saida = open('a_small.out', 'w')

quantos = int(arquivo.readline())

for i in range(1,quantos+1):
    plugs, vezes = [int(x) for x in arquivo.readline().split()]
    
    if vezes == 2**plugs-1:
        resultado = "ON"
    else:
        if vezes/2**plugs*2**plugs+2**plugs-1 == vezes:
            resultado = "ON"
        else:
            resultado = "OFF"
    
    saida.write('Case #%i: %s\n' % (i, resultado))


arquivo.close()
saida.close()