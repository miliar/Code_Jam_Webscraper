#!/usr/bin/env python

import itertools
from fractions import gcd

def optimal(L):
    difs = (abs(x[0]-x[1]) for x in itertools.combinations(L, 2))

    g = difs.next()

    for dif in difs:
        g = gcd(g, dif)

    return g

def next_optimal(L):
    op = optimal(L)
    n = L[0] % op
    if n:
        return op - (L[0] % op)
    else:
        return n


if __name__ == '__main__':
    import sys

    f = open(sys.argv[1], 'r')

    lines = enumerate(f.readlines())
    lines.next()

    for i, line in lines:
        data = [long(n) for n in line.strip().split()[1:]]
        print "Case #%s: %s" % (i, next_optimal(data))
