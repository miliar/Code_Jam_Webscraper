#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sys import stdin

Amax = 10000
Bmax = 10000

count = int(stdin.readline().strip())
for i in range(count):
    wirecount = int(stdin.readline().strip())
    wires   = []
    crosses = 0
    #left  = [None] * Amax
    #right = [None] * Bmax

    # load wires
    for j in range(wirecount):
        a, b = map(lambda x: int(x)-1, stdin.readline().strip().split())
        assert(a >= 0 and a < Amax)
        assert(b >= 0 and a < Bmax)

        for a2,b2 in wires:
            if a < a2 and b < b2:
                continue
            if a > a2 and b > b2:
                continue
            crosses += 1
        wires.append((a,b))
        #left[a]  = j
        #right[b] = j

    print("Case #{0}: {1}".format(i + 1, crosses))
