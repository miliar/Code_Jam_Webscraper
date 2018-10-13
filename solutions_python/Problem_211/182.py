#!/bin/python
import sys
input_filename, = sys.argv[1:]
input = open(input_filename)
assert input_filename.endswith('.in'), input_filename
output = open(input_filename[:-3]+'.out', 'w')

from collections import defaultdict

def Pfun(K, P):
    if K == 0:
        return 1.0
    if K > len(P):
        return 0.0
    if K == len(P):
        p = 1.0
        for q in P:
            p *= q
        return p
    P0, P = P[0], P[1:]
    p = 0.0
    if P0 > 0.0:
        p += P[0] * Pfun(K-1, P)
    if P0 < 1.0:
        p += (1.0 - P0) * Pfun(K, P)

def run():
    N, K = map(int,input.readline().split())
    U = float(input.readline())
    P = map(float, input.readline().split())
    P.sort()
    print "P=", P

    while U > 0.0:
        i = 1
        while i<len(P) and P[i] <= P[0]:
            i += 1
        amount = U/i
        if i<len(P) and P[0] + amount > P[i]:
            U -= i*(P[i] - P[0])
            for k in range(i):
                P[k] = P[i]
        else:
            U = 0.0
            for k in range(i):
                P[k] += amount
    return Pfun(K, P)
    
T = int(input.readline())
for t in range(T):
    print >> output, 'Case #{}: {}'.format(t+1,run())
