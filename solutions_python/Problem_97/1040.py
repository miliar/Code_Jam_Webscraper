'''
Created on 14/04/2012

@author: david
'''
import time
from problemaC.Reverso import Reverso

def contruyeReversos(min,max):
    salida = []
    for item in range(min, max+1):
        reverso = Reverso(item, min, max)
        reverso.construyeListaReversos()
        salida.append(reverso)
    return salida

def cuentaCasos(reverso):
    return len(reverso.getListaReversos()) 

def transfEntero(lista):
    salida = []
    for i in lista:
        salida.append(int(i))
    return salida

if __name__ == "__main__":
    #tiempo = time.time()
    fileIn = open("C-small-attempt0.in")
    iter = int (fileIn.readline())
    l = range(iter)
    listaEntrada =[]
    listaPrincipal = []
    listaSalida = []
    for i in l:
        cad = fileIn.readline()
        cad = cad[:-1]
        auxList = cad.split(" ")
        auxList = transfEntero(auxList)
        listaEntrada.append(auxList)
    fileIn.close()
    for item in listaEntrada:
        l = contruyeReversos(item[0], item[1])
        listaPrincipal.append(l)
    for item in listaPrincipal:
        numReversos = 0
        for rever in item:
            numReversos += cuentaCasos(rever)
        listaSalida.append(numReversos/2)
    fileOut = open("C-small-attempt0.out",'w')
    for i in range(len(listaSalida)):
        fileOut.writelines("Case #%d: %s" % (i + 1, listaSalida[i])+'\n')
    fileOut.close()
    #print 'tiempo: ', time.time() -tiempo