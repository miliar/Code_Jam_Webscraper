import sys
if len(sys.argv) > 1:
    entrada = open(sys.argv[1])
else:
    entrada = open('c.in')
T = int(entrada.readline())

from heapq import heappush, heappop, heapreplace


for caso in xrange(1, T + 1):
    linea = entrada.readline().strip()
    N, K = map(int, linea.split(' '))

    q = []

    maxLR = 0
    minLR = 0

    tramo = N
    for i in xrange(K):
        if tramo % 2 == 0:
            maxLR = tramo / 2
            minLR = tramo / 2 - 1
        else:
            maxLR = (tramo - 1) / 2
            minLR = maxLR
        if maxLR == 0:
            break
        heappush(q, -maxLR)
        tramo = -heapreplace(q, -minLR)
    print "Case #{}: {} {}".format(caso, maxLR, minLR)
