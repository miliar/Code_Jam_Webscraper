entrada = open("C-small-attempt0.in") 
salida = open("c.out", 'w')
for case in xrange(1, int(entrada.readline())+1):
    salida.write("Case #"+str(case)+": ")
    n, q = map(int, entrada.readline().split())
    caballos = [map(int, entrada.readline().split()) for _ in xrange(n)]
    distancias = [[int(x) for x in entrada.readline().split()] for _ in xrange(n)]
    dists = [distancias[i][i+1] for i in xrange(n-1)]
    qs = [map(int, entrada.readline().split()) for _ in xrange(q)]
    llegada = [float("inf")]*n
    llegada[0] = 0
    ac = 0
    acdists = [0]
    for i in xrange(n-1):
        acdists.append(acdists[-1]+dists[i])
        
    for i in xrange(1, n):
        ac += dists[i-1]
        res = float("inf")
        for j in xrange(i):
            caballos[j][0] -= dists[i-1]
            if caballos[j][0] >= 0:
                res = min(res, (acdists[i]-acdists[j])/float(caballos[j][1]) + llegada[j])
        llegada[i] = res
    salida.write("{0:.6f}".format(llegada[-1])+"\n")