#!/usr/bin/python

import sys

def enteroCero(a):
    if (a < 10):
        return ("0" + str(a))
    else:
        return (str(a))

#para sumar horas
def sumahora(horaA,horaB):
    horas = int(horaA[:2]) + int(horaB[:2])
    if (horas > 23):
        horas -= 24
    minutos = int(horaA[-2:]) + int(horaB[-2:])
    if (minutos > 59):
        minutos -= 60
        horas += 1

    resultado = enteroCero(horas) + ":" + enteroCero(minutos)

    return resultado 


# las cantidades de trenes de una estacion X
def cantidad(salida, llegada, vuelta):
    #print "llamada :"
    #print salida
    #print llegada
    #print vuelta
    if (len(salida) == 0):
        return 0
    if (len(llegada) == 0):
        return len(salida)
    salida.sort()
    llegada.sort()
    listo = []
    for tren in llegada:
        listo += [sumahora(tren, ("00:" + enteroCero(vuelta)))]
    cant = len(salida)
    conta = 0
    contb = 0
    while ((contb < len(listo)) & (conta < len(salida))):
        #print "comparacion : " + listo[contb] + " " + salida[conta]
        if (listo[contb] <= salida[conta]):
            #print "verdadero"
            cant -= 1        
            contb += 1
        conta += 1            
    if (cant < 0):
        return 0
    else:
        return cant

# funcion para encontrar la cantidad de trenes
def cantTrenes(vuelta, tripsA, tripsB):
    salidaA = []
    llegadaA = []
    for trip in tripsA:
        salidaA += [trip[0]]
        llegadaA += [trip[1]]
    salidaB = []
    llegadaB = []
    for trip in tripsB:
        salidaB += [trip[0]]
        llegadaB += [trip[1]]
    cantA = cantidad(salidaA, llegadaB, vuelta)
    cantB = cantidad(salidaB, llegadaA, vuelta)
    return [cantA, cantB]

# main 

if (len(sys.argv) != 3):
    print "forma de uso TrainTimeTable.py entrada.in salida.out"
    sys.exit(0)

archEntrada = sys.argv[1]
archSalida = sys.argv[2]
    
entrada = open(archEntrada,"r")
salida = open(archSalida, "w")
    
# cantidad de casos de prueba 
cant = int(entrada.readline())
#print cant

for cont in range(1, cant + 1):
    # cantidad de minutos de la vuelta
    vuelta = int(entrada.readline())
    temp = entrada.readline().split()
    NA = int(temp[0])
    NB = int(temp[1])
    tripsA = []
    for contb in range(NA):
        tripsA += [entrada.readline().split()]

    tripsB = []
    for contb in range(NB):
        tripsB += [entrada.readline().split()]    
    
    n = cantTrenes(vuelta, tripsA, tripsB)
    resultado = "Case #" + str(cont) + ": " + str(n[0]) + " " + str(n[1])
    print resultado
    salida.write(resultado + "\n")

entrada.close()
salida.close()
