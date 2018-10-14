import sys

fname = sys.argv[1]

def itero(fn):
    with open(fname) as f:
        i = 0
        for line in f:
            if i > 0:
                x = line.strip()
                fn(i, x)
            i += 1

import math
def e_pow(x): return int(math.log10(x)) + 1

def cycle(x, k, n): 
    n10 = (10 ** n)
    return x / n10 + x % n10 * (10 ** (k - n))

def inr(a, b):
    m = e_pow(a)
    s = set([])
    for i in xrange(a, b + 1):
        for k in range(1, m):
            l = cycle(i, m, k)
            if l > i and a <= l <= b: 
                s.add((i,l))
                #print i, l, i == l, a <= l <= b
    return len(s)

def inr2(a, b):
    m = e_pow(a)
    s = set([])
    prange = range(1, m)
    for k in prange:
        n10 = (10 ** k)
        r10 = (10 ** (m - k))
        for i in xrange(a, b + 1):
            l = i / n10 + i % n10 * r10
            if l > i and a <= l <= b: 
                s.add((i, l))
    return len(s)

def pro(x):
    return inr2(*x)

def problemC(i, s):
    r = pro([int(e) for e in s.split()])
    print ("Case #%i:" % i), r


import time
kt = time.clock()
#print inr(1000000, 1999999)
#print kt, time.clock(), " === ", time.clock() - kt
#kt = time.clock()
#print inr2(1000000, 1999999)
#print inr2(100, 500)
#print inr2(1111, 2222)
itero(problemC)
#print kt, time.clock(), " === ", time.clock() - kt



