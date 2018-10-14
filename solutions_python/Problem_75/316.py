import collections
import sys

sys.stdout = open("salida.out","w")

handle = open("entrada.in")

casos = int(handle.readline())
for caso in xrange(1,casos+1):
    linea = iter(handle.readline().split())
    cantcomb = int(linea.next())
    combis = {}
    for _ in xrange(cantcomb):
        a,b,c = (x for x in linea.next())
        combis[(a,b)] = c
        combis[(b,a)] = c
    cantopp = int(linea.next())
    opps = collections.defaultdict(set)
    for _ in xrange(cantopp):
        a,b = (x for x in linea.next())
        opps[a].add(b)
        opps[b].add(a)
    n = int(linea.next())
    cosas = linea.next()
    lista = []
    
    for cosa in cosas:
        lista.append(cosa)
        if len(lista) > 1:
            a = lista[-1]
            b = lista[-2]  
            if (a,b) in combis:
                lista[-2:] = [combis[(a,b)]]
            else:
                for x in lista[:-1]:
                    if x in opps[cosa]:
                        lista = []
    print "Case #%s: [%s]" % (caso, ", ".join(lista)) 