from math import *

T = int(raw_input())
for i in xrange(T):
    n, p = map(int, raw_input().split())
    guar = 0
    if p > 2**(n - 1):
        at = 2**(n - 1)
        for j in xrange(n - 2, -1, -1):
            at += 2**j
            if p <= at:
                guar = 2**(n - 1 - j + 1) - 2
                break
        else:
            guar = 2**n - 1
    poss = 2**n - 2**(n - int(log(p, 2)))
    print "Case #%d: %d %d" % (i + 1, guar, poss)

