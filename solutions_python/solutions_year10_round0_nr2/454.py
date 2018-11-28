#!/usr/bin/env python
import sys

T = int(sys.stdin.readline())


def gcd(a,b):
    while a != 0:
        a,b = b % a, a
    return b

for tt in xrange(T):
    inp = [int(x) for x in sys.stdin.readline().split()]
    N = inp[0]
    t = inp[1:]
    t.sort()
    tnew = t[1:]
    for i in xrange(len(tnew)):
        tnew[i] = tnew[i] - t[0]
    if len(tnew) == 1:
        g = tnew[0]
    else:
        g = gcd(tnew[0],tnew[1])
        for i in xrange(2,len(tnew)):
            g = gcd(g,tnew[i])

    if g == 1:
        res = 0
    else:
        res = (g - t[0] % g) % g

    u = t
    for i in xrange(len(t)):
        u[i] = t[i] + res
    print "Case #%d: %d" % (tt+1, res)
    


