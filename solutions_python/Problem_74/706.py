#!/usr/bin/python

import sys
import os.path

def contarTiempo(n, t, p):
    po = 1 # pocision orange
    pb = 1 # pocision blue
    ct = 0 # contador tiempo
    to = 0 # tiempo orange
    tb = 0 # tiempo blue

    for paso in p:
        if paso[0] == "O":
            if abs(paso[1] - po) > (ct - to):
                ct += abs(paso[1] - po) - (ct - to) + 1
            else:
                ct += 1
            po = paso[1]
            to = ct
        elif paso[0] == "B":
            if abs(paso[1] - pb) > (ct - tb):
                ct += abs(paso[1] - pb) - (ct - tb) + 1
            else:
                ct += 1
            pb = paso[1]
            tb = ct
    return ct

# Esta es mi solucion en python del problema Bot Trust del code jam del 2011

archsalida = "*.out"
linea = ""

# que tome el nombre del archivo de la linea de comandos
if (len(sys.argv) != 2):
    print " solo se necesita el archivo de entrada como prametro"
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
n = int(entrada.readline().replace("\n", ""))
# se lee la siguiente linea 
linea = entrada.readline()
cont = 0
while ((linea != "") & (cont < n)):

    # hay que leer la fila
    fila = linea.replace("\n","").split(" ")

    # el primer valor de la fila es la cantidad de pasos T
    t = int(fila[0])

    # a partir de ahi hay que tomar parejas
    p = []
    i = 1
    while i < len(fila):
        p += [(fila[i], int(fila[i + 1]))]
        i += 2

    # se procesa el caso
    resultado = contarTiempo(n, t, p)

    # se pone la salida del caso
    salida.write ("Case #%i: %s\n" % ((cont + 1), resultado) )
    cont += 1
    linea = entrada.readline()

# se cierran los archivos
entrada.close()
salida.close()
