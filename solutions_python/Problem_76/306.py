import collections
import sys

sys.stdout = open("salida.out","w")

handle = open("entrada.in")

casos = int(handle.readline())
for caso in xrange(1,casos+1):
    handle.readline()
    numeros  = [int(x) for x in handle.readline().split()]
    valor = reduce(lambda x,y: x^y, numeros)
    if valor == 0:
        res = sum(numeros) - min(numeros)
    else:
        res = "NO"
    print "Case #%s: %s" % (caso, res) 