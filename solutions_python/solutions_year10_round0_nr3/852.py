#!/usr/bin/python

import sys
import os.path

def casoThemePark(R, k, N, g):
    fila = g[:]
    c = 0
    posa = 0
    posb = 0
    poss = 0
    ganancia = 0
    cantidad = 0

    print " caso: R=%i k=%i N=%i g=%s" % (R, k, N, g)

    # que cuente R iteraciones
    while (c < R):
        # se arma un vagon con la cantidad de personas k

        cantidad = 0
        posa = posb
        # mientras el grupo quepa sin sobrepasar k
        while ((cantidad + fila[posb]) <= k):

            # se suma la cantidad de personas en el grupo
            cantidad += fila[posb]

            print "vuelta %i incluye grupo %i" % (c, fila[posb])

            # se calcula el indice siguiente
            poss = posb + 1
            if (poss == len(fila)):
                poss = 0
            
            # si el indice siguiente es la posicion inicial
            if (posa == poss):                
                # sale del bucle
                break
            else:
                # si no entonces posb toma la poss
                posb = poss
        # se suman las ganancias
        ganancia += cantidad
        
        c += 1

    return ganancia


# Esto es una plantilla para los programitas de code jam para
# poner un par de cositas que son comunes a todos los programitas

archsalida = "*.out"
linea = ""
filan = []
filan2 = []
contenido = []
contenidon = []
resultado = []

# que tome el nombre del archivo de la linea de comandos
if (len(sys.argv) != 2):
    print " la forma de uso es: $ ./script.py entrada.in"
    sys.exit(0)

# si el archivo no existe que se queje y salga
if (not os.path.exists(sys.argv[1])):
    print " no existe el archivo " + sys.argv[1]
    sys.exit(0)

# si existe que lo abra para lectura
entrada = open(sys.argv[1], "r");

# eligiendo el nombre del archivo de salida
if ("." in sys.argv[1]):
    archsalida = sys.argv[1].split(".")[0]
else:
    archsalida = sys.argv[1]

archsalida += ".out"

# abriendo el archivo para escribir
salida = open(archsalida, "w");

# normalmente la primera linea dice la cantidad de casos
cantidad = int(entrada.readline().replace("\n", ""))
# se lee la siguiente linea 
linea = entrada.readline()
cont = 0
while ((linea != "") & (cont < cantidad)):
    # se necesitan dos lineas por caso

    # procesando la linea uno
    fila = linea.replace("\n","").split(" ")
    filan = []
    for valor in fila:
        if (valor.isdigit()):
            filan += [int(valor)]

    # leyendo la linea 2
    linea = entrada.readline()
    if (linea == ""):
        # un caso incompleto ?
        break
    
    fila = linea.replace("\n","").split(" ")
    filan2 = []
    for valor in fila:
        if (valor.isdigit()):
            filan2 += [int(valor)]

    # se procesa el caso
    resultado = casoThemePark(filan[0], filan[1], filan[2], filan2)

    # se pone la salida del caso
    salida.write ("Case #%i: %s\n" % ((cont + 1), resultado) )
    cont += 1
    linea = entrada.readline()

# se cierran los archivos
entrada.close()
salida.close()
