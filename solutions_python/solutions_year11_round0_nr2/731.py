#!/usr/bin/python

import sys
import os.path

# Esto es una plantilla para los programitas de code jam para
# poner un par de cositas que son comunes a todos los programitas

def magicka(c, d, cant, mezcla):
    resultado = ""
    ind = 2
    
    while ind <= len(mezcla):
        # primero las sustituciones
        for comb in c:
            if (mezcla[ind - 2:ind] == comb[0]) or (mezcla[ind -2:ind] == comb[0][1] + comb[0][0]):
                mezcla = mezcla[:ind - 2] + comb[1] + mezcla[ind:]
                ind -= 1

        # despues las eliminaciones        
        for elim in d:
            print "nuevo"
            print len(mezcla)
            print ind
            print ind - 1
            print ind - 2
            if (len(mezcla) == 0):
                break
            if ((mezcla[ind - 1] == elim[0]) and (elim[1] in mezcla[:ind - 1])) or ((mezcla[ind - 1] == elim[1]) and (elim[0] in mezcla[:ind - 1])):
                mezcla = mezcla[ind:]
                ind = 1
        ind += 1
    ind = 0
    while ind < (len(mezcla) - 1):
        resultado += mezcla[ind] + ", "
        ind += 1
    resultado = "[" + resultado + mezcla[-1:] + "]"
    return resultado

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
    # se lee la linea del caso
    fila = linea.replace("\n","").split(" ")

    c = [] # combinaciones
    d = [] # eliminaciones
    cant = 0
    mezcla = "" # cadena con las mezclas

    i = 0
    cc = int(fila[i]) + i + 1 # cantidad de combinaciones
    i += 1
    while i < cc:
        c += [(fila[i][0] + fila[i][1], fila[i][2])]
        i += 1

    cd = int(fila[i]) + i + 1 # cantidad de eliminaciones
    i += 1
    while i < cd:
        d += [fila[i][0] + fila[i][1]]
        i += 1

    cant = int(fila[i])
    i += 1
    mezcla = fila[i]
    
    # se procesa el caso
    resultado = magicka(c, d, cant, mezcla)

    # se pone la salida del caso
    salida.write ("Case #%i: %s\n" % ((cont + 1), resultado) )
    cont += 1
    linea = entrada.readline()

# se cierran los archivos
entrada.close()
salida.close()
