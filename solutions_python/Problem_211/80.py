import math, collections, copy, sys
from decimal import Decimal
f = open('input.in','r')
g = open('output.txt','w')
"""

"""
for index in xrange(1, int(f.readline()[:-1]) + 1):
    N, K = [int(x) for x in f.readline()[:-1].split(' ')]
    U = Decimal(f.readline()[:-1])
    P = sorted([Decimal(x) for x in f.readline()[:-1].split(' ')])

    for i in xrange(N-1):
        if U > (i+1)*(P[i+1]-P[i]):
            U -= (i+1)*(P[i+1]-P[i])
            add = P[i+1]-P[i]
            for j in xrange(i+1):
                P[j] += add
        else:
            add = U / (i+1)
            U = 0
            for j in xrange(i+1):
                P[j] += add
            break
    if U > 0:
        P = [P[0] + U/N] * N
    prod = 1
    for p in P:
        prod *= p
    result = str("{:.7f}".format( prod ))



    
    g.write("Case #{}: {}\n".format(index, result))
    print "Case #{}: {}\n".format(index, result)
f.close()
g.close()