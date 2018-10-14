import math, collections, copy, sys
from decimal import Decimal
f = open('input.in','r')
g = open('output.txt','w')
"""

"""
for index in xrange(1, int(f.readline()[:-1]) + 1):
    N, C, M = [int(x) for x in f.readline()[:-1].split(' ')]
    B = [0]*M
    P = [0]*M
    count = [0]*C
    positions = [0]*N
    for i in xrange(M):
        B[i], P[i] = [int(x) for x in f.readline()[:-1].split(' ')]
        count[P[i]-1] += 1
        positions[B[i]-1] += 1
    q = copy.deepcopy(positions)
    s = [0]*N
    s[0] = q[0]
    for i in xrange(1, N):
        s[i] = s[i-1] + q[i]
        q[i] = int(math.ceil(1.0*s[i]/(i+1)))
    y = max(max(count), max(q))
    result = str(y) + ' ' + str(max((x>y)*(x-y) for x in positions))
    g.write("Case #{}: {}\n".format(index, result))
    print "Case #{}: {}\n".format(index, result)
f.close()
g.close()