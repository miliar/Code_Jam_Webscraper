"""
Ejercicio 2
"""

import sys

def log(cadena):
    """ Muestra cadena por sys error """
    print >> sys.stderr, cadena
    pass

def donde_rompe(cadena):
    for i in xrange(len(cadena)-1):
        if cadena[i] > cadena[i+1]:
            return i
    return -1

def caso(linea):
    """ Resuelve un caso concreto """
    # P = map(int,P.split(" "))
    # (pancakes, sK) = linea.split(" ")
    N = linea
    rompe_en = donde_rompe(linea)
    if rompe_en == -1:
        return linea

    log("N = %s " % (linea))

    cifra = str(int(linea[rompe_en]) - 1)

    log("rompe en %d , cifra %s" % (rompe_en, cifra))
    log("exp = %d " % (len(linea) - rompe_en))
    log(" len = %d " % (len(linea)))
    novo = linea[:rompe_en] + cifra + '9'*(len(linea)-rompe_en-1)
    return caso(novo.lstrip('0'))

def problema():
    """ Funcion principal """
    namefile = "B-large"
    fichero = open(namefile + ".in", "r")

    casos = int(fichero.readline())

    for i in xrange(1, casos+1):

        log("---------- Caso %d de %d" % (i, casos))

        linea = fichero.readline().rstrip('\n')
        print "Case #%d: %s" % (i, caso(linea))


if __name__ == "__main__":
    # print donde_rompe("54")
    problema()
