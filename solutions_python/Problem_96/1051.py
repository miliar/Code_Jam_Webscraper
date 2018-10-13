'''
Created on 13/04/2012

@author: david
'''
from problemaB.Tripleta import Tripleta
import threading
import time
from problemaB2.MergeSort import mergesort


def retornaCasosSupUmbral(listaTripleta, umbral, numEspeciales):
    casos = 0
    casosEspeciales = 0
    listaNoSuperaron =[]
    casosSuperados = []
    for  trip in listaTripleta:
        if trip.getSupera():
            casos +=1
        else:
            listaNoSuperaron.append(trip)
    if(casosEspeciales < numEspeciales):
        #listaNoSuperaron = mergesort(listaNoSuperaron)
        listaNoSuperaron.sort(key = lambda x: x.getSuma(), reverse = True)
        listaHebras = []
        for trip in listaNoSuperaron:
            if casosEspeciales < numEspeciales:
                casosEspeciales += 1
                hebra = threading.Thread(target = convierteEspeciales, args=(trip, umbral, casosSuperados))
                listaHebras.append(hebra)
                hebra.start()
                
            else:
                break
        for h in listaHebras:
            h.join()
    casos += len(casosSuperados)
    return casos

def convierteEspeciales(trip, umbral,lista):
    trip.convierteSorpresa()
    trip.superaExpec(umbral)
    if trip.getSupera():
        lista.append(1)
    return

def transformaInt(lista):
    salida = []
    for i in lista:
        salida.append(int(i))
    return salida

def manejaTripleta(listaTripletas, suma, umbral):
    tripleta = Tripleta(suma)
    tripleta.superaExpec(umbral)
    listaTripletas.append(tripleta)
         

if __name__ == "__main__":
    tiempo = time.time()
    fileIn = open("B-large.in")
    fileOut = open("B-large.out",'w')
    iter = int (fileIn.readline())
    l = range(iter)
    listCasosSuperaUmbral =[]
    for i in l:
        numCasosSupUmbral = 0
        casosEspeciales = 0
        umbral = 0
        cad = fileIn.readline()
        cad = cad[:-1]
        auxList = cad.split(" ")
        auxList = transformaInt(auxList)
        googlers = auxList[0]
        casosEspeciales =  auxList[1]
        umbral = auxList[2]
        auxList2 = auxList[3:]
        auxList2.sort()
        esEspecial = True
        listaTripletas = []
        listaHebras = []
        for suma in auxList2:
            hebra = threading.Thread(target = manejaTripleta, args = (listaTripletas,suma, umbral))
            listaHebras.append(hebra)
            hebra.start()
        for h in listaHebras:
            h.join()
            
        numCasosSupUmbral = retornaCasosSupUmbral(listaTripletas, umbral, casosEspeciales)
        listCasosSuperaUmbral.append(numCasosSupUmbral)
    fileIn.close()
    for i in range(len(listCasosSuperaUmbral)):
        fileOut.writelines("Case #%d: %s" % (i + 1, str(listCasosSuperaUmbral[i]))+'\n')
    fileOut.close()
    print time.time() -tiempo
        
