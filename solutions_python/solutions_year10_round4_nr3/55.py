#! /usr/bin/env python

from __future__ import division, print_function

for case in xrange(1, int(raw_input())+1):
    nrects = int(raw_input())
    bac = set()
    for r in xrange(nrects):
        x1, y1, x2, y2 = map(int, raw_input().split())
        for x in xrange(x1, x2+1):
            for y in xrange(y1, y2+1):
                bac.add((x, y))
    time = 0
    # for x in xrange(1,7):
    #     for y in xrange(1,7):
    #         print(1 if (y, x) in bac else 0, end="")
    #     print()
    # print()
    while len(bac) > 0:
        oldbac = set(bac)
        for x, y in oldbac:
            if (x-1, y+1) in oldbac:
                bac.add((x, y+1))
            if (x+1, y-1) in oldbac:
                bac.add((x+1, y))
        for x, y in oldbac:
            if not ((x-1, y) in oldbac or (x, y-1) in oldbac):
                bac.remove((x, y))
        # for x in xrange(6):
        #     for y in xrange(6):
        #         print(1 if (x, y) in bac else 0, end="")
        #     print()
        # print()
        time += 1
    print("Case #{0}:".format(case), time)
