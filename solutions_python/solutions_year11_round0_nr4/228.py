from decimal import *
from math import factorial
import sys

sys.setrecursionlimit(5000)

C = dict()
C[(0, 0)] = 1
C[(1, 0)] = 1
C[(1, 1)] = 1

d = dict()
d[0] = 1
d[1] = 0
d[2] = 1
d[3] = 2

a = dict()
a[0] = Decimal(0).quantize(Decimal('1.000000'))

def binomial(n, k):
    global C
    if (n, k) not in C:
        if (n == k) or (k == 0):
            C[(n, k)] = 1
        else:
            C[(n, k)] = binomial(n-1, k-1) + binomial(n-1, k)
    return C[(n, k)]

def derangement(n):
    global d
    if n not in d:
        d[n] = n * derangement(n-1) + pow(-1, n)
    return d[n]

#Partial Derangement
def pd(n, k):
    return binomial(n, k) * derangement(n-k)

def ans(n):
    global a
    if n not in a:
        result = Decimal(1)
        for i in xrange(n+1):
            #print n-i, pd(n,i), factorial(n)
            result = result + (Decimal(str((n-i)*pd(n,i))) / Decimal(str(factorial(n))));
        a[n] = result.quantize(Decimal('1.000000'))
    return a[n]
        

fileName = "D-large"
fin = open(fileName + ".in", "r")
fout = open(fileName + ".out", "w")

T = int(fin.readline())

for caseID in xrange(1, T+1):
    N = int(fin.readline())
    k = 0
    seq = map(int, fin.readline().split())
    for i in xrange(N):
        if seq[i] != i+1:
            k += 1
    print "Case #%d: %s" % (caseID, ans(k))
    fout.write("Case #%d: %s\n" % (caseID, ans(k)))

fin.close()
fout.close()

#raw_input()
