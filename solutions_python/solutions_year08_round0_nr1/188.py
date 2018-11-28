#!/usr/bin/python

import sys

# la solucion iterativa
# buscando proxima zona mas grande sin cambios
def cantMinCambios(buscadores, queries):
    print "llamada: "
    print buscadores
    print queries
    # existe alguno que no este en los queries
    for buscador in buscadores:
        if (buscador not in queries):
            return 0
    cont = 0
    pos = -1
    cambios = 0
    valores = [-1] * len(buscadores)
    while (cont < len(queries)):
        contb = 0
        while (contb < len(buscadores)):
            if ((queries[cont] == buscadores[contb]) & (valores[contb] == -1)):
                valores[contb] = cont
            contb += 1
        if (-1 not in valores):            
            cambios += 1
            contb = 0         
            while (contb < len(buscadores)):
                if (valores[contb] > valores[pos]):
                    pos = contb                    
                contb += 1
            valores = [-1] * len(buscadores)
            valores[pos] = 0
        print valores
        print queries[cont]
        print str(cont) + "cambios: " + str(cambios)
        cont += 1
    print "retorno: "
    print cambios
    return cambios

# la solucion recursiva (me mato con el tiempo :))
def cantMinCamb(buscadores, queries, marginado = []):
    #    print "llamada: "
    #    print buscadores
    #    print queries
    #    print marginado
    if (queries == []):
        return 0
    # existe alguno que no este en los queries
    for buscador in buscadores:
        if (buscador not in queries):
            return 0
    casos = []
    for caso in buscadores:
        corte = queries.index(caso)
        tbuscadores = buscadores[:] + marginado
        tbuscadores.remove(caso)
        tqueries = queries[corte:]
        casos += [1 + cantMinCamb(tbuscadores,tqueries,[caso])]
    casos.sort()
    #    print "retorno: "
    #    print casos
    return casos[0]

# main 

if (len(sys.argv) != 3):
    print "forma de uso SavingTheUniverse.py entrada.in salida.out"
    sys.exit(0)

archEntrada = sys.argv[1]
archSalida = sys.argv[2]
    
entrada = open(archEntrada,"r")
salida = open(archSalida, "w")
    
# cantidad de casos) de prueba 
cant = int(entrada.readline())
#print cant

for cont in range(1, cant + 1):
    # cantidad de search engines
    cantS = int(entrada.readline())
    buscadores = []
    for contb in range(cantS):
        valor = entrada.readline()
        if (valor[-1:] == "\n"):
            valor = valor[:-1]
        buscadores += [valor]
    print "buscadores"
    print buscadores 
    # cantidad de queries
    cantQ = int(entrada.readline())
    queries = []
    for contb in range(cantQ):
        valor = entrada.readline()
        if (valor[-1:] == "\n"):
            valor = valor[:-1]
        queries += [valor]
    print "queries"
    print queries
    #n = cantMinCamb(buscadores, queries)
    n = cantMinCambios(buscadores, queries)
    resultado = "Case #" + str(cont) + ": " + str(n) 
    print resultado
    salida.write(resultado + "\n")

entrada.close()
salida.close()
