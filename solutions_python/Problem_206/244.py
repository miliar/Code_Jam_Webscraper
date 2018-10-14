entrada = open("A-large.in") 
salida = open("a.out", 'w')
for case in xrange(1, int(entrada.readline())+1):
    salida.write("Case #"+str(case)+": ")
    d, n = map(int, entrada.readline().split())
    caballos = [tuple(map(int, entrada.readline().split())) for _ in xrange(n)]
    caballos.sort()
    distancias = []
    maxdist = 0
    for c in reversed(caballos):
        dist = (d - c[0])/float(c[1])
        maxdist = max(maxdist, dist)
    salida.write("{0:.6f}".format(round(d/float(maxdist),6))+"\n")
