#!/usr/bin/python

## Interpreter: Python 2.6.5

from fractions import gcd

T = int(raw_input())
for c in range(1, T + 1) :
    args = raw_input().split()
    N = int(args[0])
    t = [ int(args[i + 1]) for i in range(N) ]
    dt = [ abs(t[i + 1] - t[i]) for i in range(N - 1) ]
    T = reduce(gcd, dt)
    maxt = max(t)
    if maxt % T == 0 :
        ans = 0
    else :
        ans = (maxt / T + 1) * T - maxt
    print "Case #{0}: {1}".format(c, ans)

