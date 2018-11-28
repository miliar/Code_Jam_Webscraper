#!/usr/bin/python
import math
import sys
from fractions import gcd

# Log base 2 of
def pow2lte(n):
    i = 0
    p = 1
    while (p <= n):
        p = p << 1
        i += 1
    return i-1

T = int(sys.stdin.readline())
for i in xrange(T):
    print "Case #%d:" % (i+1),
    P,Q = map(int, sys.stdin.readline().strip().split("/"))
    if P <= 0:
        print "impossible"
        continue
    G = gcd(P,Q)
    P /= G
    Q /= G
    if (math.pow(2, 40) % Q != 0):
        print "impossible"
    else:
        P *= math.pow(2,40)/Q
        pow2count = pow2lte(P)
        print (40-pow2count)
