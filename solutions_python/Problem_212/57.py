#!/usr/bin/python

from __future__ import division
from gcj import *

# boolean flags, reachable via OPTS.flagname. Space separated in string
FLAGS = ''

def case():
    N, P = ints()
    G = ints()
    good = 0
    persize = [0] * P
    for g in G:
        persize[g % P] += 1
    print persize
    good += persize[0]
    persize[0] = 0

    good += solve(0, persize)

    return good

cache = {}
def solve(offset, persize):
    key = (offset, tuple(persize))
    if key in cache:
        return cache[key]
    P = len(persize)
    bestsofar = 0
    for i in range(1, P):
        if persize[i]:
            npersize = persize[:]
            npersize[i] -= 1
            r = solve((offset + i) % P, npersize)
            if offset == 0:
                r += 1
            if r > bestsofar:
                bestsofar = r

    #print "S: %r, %r -> %r" % (offset, persize, bestsofar)
    cache[key] = bestsofar
    return bestsofar

if __name__ == '__main__':
    main()
