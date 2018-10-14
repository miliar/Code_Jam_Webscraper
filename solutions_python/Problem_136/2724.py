#coding=UTF-8
__author__ = 'jesus'

FILE = 'qual-b.in'
FILEOUT = 'qual-b.out'

"""
En cada momento se puede, o ahorrar para construir una fabrica y conseguir una nueva rate,
o seguir como se esta
"""

RATE_NORMAL = 2.0


f = open(FILE, 'r')
fout = open (FILEOUT, 'w')

def calcular (cost_factory, rate_factory, amount):
    rate = RATE_NORMAL
    construction = 0
    i = 0
    #time for i factory creation
    time = amount / rate
    newtime = time
    while newtime<=time:
        i += 1
        time = newtime
        construction += cost_factory / rate
        rate += rate_factory
        newtime = construction + amount / rate
        #print "with ", i, "constructions, ", construction, " + ", amount/rate, "=", newtime
    print "total time", time
    return time

#print calcular (500.0, 4.0, 2000.0)
#print calcular (30.0, 1.0, 2.0)

testcases = int(f.next())
for icase in range (1, testcases+1):
    print "Case ", icase
    C, F, X = map (float, f.next().split())
    print "Case #{0}: ".format (icase, calcular(C, F, X ))
    fout.write ("Case #{0}: {1:.7f}\n".format (icase, calcular(C, F, X )))


f.close()
fout.close()
