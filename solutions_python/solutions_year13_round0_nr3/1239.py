'''
Created on 13/04/2013

@author: Javier
'''

import math

archivo = "C-small-attempt0.in"
entrada = file(archivo)


def palindrome(number):
    cadena = str(number)
    longitud = len(cadena)
    simetria = longitud /2
    valido = True
    
    for i in range(0, simetria):
        if cadena[i] != cadena[longitud - 1 - i]:
            valido = False
            break
    
    return valido

def buscaPalindrome(limite0, limite1, caso):
    
    contador = 0
    
    for i in range(limite0, limite1 + 1):
        
        if palindrome(i):
            #i es el cuadrado de un palindrome
            raiz = math.sqrt(i)
            if raiz % 1 != 0: #no es entero
                continue
             
            if palindrome(int(raiz)):
                contador = contador + 1
    
    
    print "Case #" + str(caso) + ": " + str(contador)



casos = int(entrada.readline())

for i in range(casos):
    
    info = entrada.readline().split()
    
    limite0 = int(info[0])
    limite1 = int(info[1])
    
    buscaPalindrome(limite0, limite1, i + 1)