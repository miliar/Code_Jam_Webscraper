#!/usr/bin/python

import sys
import os.path

# Esto es una plantilla para los programitas de code jam para
# poner un par de cositas que son comunes a todos los programitas

def candy(dulces):
    # print dulces
    n = len(dulces)
    pmax = 0 # pila mayor
    lim = (2 ** n) - 1
    cont = 1
    while (cont < lim):
        sp = 0 # suma patrick pila 1
        ss = 0 # suma sean pila 1
        spc = 0 # suma patrick comparacion pila 2
        # haciendo sumatoria para una posibilidad
        fbin = ("{0:0" + str(n) + "b}").format(cont)
        # print fbin
        cp = 0
        while cp < n:
            if (fbin[cp] == "0"):
                sp ^= dulces[cp]
                ss += dulces[cp]
            else:
                spc ^= dulces[cp]
            cp += 1
        # si la sumatoria de las dos pilas coincide
        # y la pila es mas grande que las anteriores
        if (sp == spc) and (ss > pmax):
            pmax = ss
        cont += 1
    if (pmax == 0):
        return "NO"
    else:
        return str(pmax)

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

    # cantidad de dulces
    cant = int(linea)

    # se lee la linea con los valores de los dulces
    linea = entrada.readline()
    dulces = []
    for valor in linea.replace("\n", "").split(" "):
        if (valor.isdigit()):
            dulces += [int(valor)]

    # se procesa el caso
    resultado = candy(dulces)

    # se pone la salida del caso
    salida.write ("Case #%i: %s\n" % ((cont + 1), resultado) )
    cont += 1
    linea = entrada.readline()

# se cierran los archivos
entrada.close()
salida.close()
