'''
abeakkas
Google CodeJam 2017 - Round 1C
Problem C
 '''
# Python candir
import sys

fin = open(sys.argv[1], 'r')
fout =  open(sys.argv[2], 'w')

T = int(fin.readline())

for iT in range(1, T + 1):
    l = fin.readline().split()
    N = int(l[0])
    K = int(l[1])
    U = float(fin.readline())
    P = [float(s) for s in fin.readline().split()]
    print(P)
    P.sort()
    while U > 0 and P[0] < 1:
        n = 0
        while n < len(P) and P[n] == P[0]:
            n += 1
        p = 0
        if n == len(P):
            p = 1
        else:
            p = P[n]
        if U > n * (p - P[0]):
            for i in range(n):
                U -= p - P[i]
                P[i] = p
        else:
            for i in range(n):
                P[i] += U / n
            U = 0
    res = 1
    for p in P:
        res *= p
    print("Case #{}: {:.10f}".format(iT, res), file=fout)
