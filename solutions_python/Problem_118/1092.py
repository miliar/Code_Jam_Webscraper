##numpy free available in http://www.numpy.org/
from numpy import *
from math import sqrt

def palindromo(numero):
    nuevo = 0
    original = numero
    while numero > 0:
        nuevo = nuevo * 10 + numero % 10
        numero = numero / 10
    if original == nuevo:
        return True
    else:
        return False


entrada = open("C-small-attempt0.in", "r")
salida = open("output.txt", "w")
casos = int(entrada.readline())
caso = 0

while caso < casos:
    a, b = map(int,entrada.readline().split())
    count = 0
    while a <= b:
        if palindromo(a):
            raiz = int(sqrt(a))
            if raiz * raiz == a:
                if palindromo(raiz):
                    count = count + 1
        a = a + 1
    salida.write("Case #"+str(caso+1)+": "+str(count)+"\n")
    caso = caso + 1

entrada.close()
salida.close()
