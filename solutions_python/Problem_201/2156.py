#!/usr/bin/env python3

import sys

sys.stdin.readline()
for (cn, ln) in enumerate(sys.stdin.readlines(), 1):
    (st, pp) = list(map(int, ln.split(' ')))
    sp = [st]
    x = None
    for i in range(pp):
        x = sp.pop(-1)
        L = (x//2)
        if L > 0:
            sp += [L]
        R = (x-L-1)
        if R > 0:
            sp += [R]
        sp.sort()
    L = (x//2)
    R = (x-L-1)
    print('Case #%s: %s %s' % (cn, L, R))
