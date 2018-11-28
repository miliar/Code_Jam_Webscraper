#!/usr/bin/env python3

from math import ceil, floor
from functools import reduce
from itertools import combinations
import sys

def solve(plts):
    best = max(plts)
    if best == 1:
        return 1
    bestd = plts

    for mins in range(1, best):
        for comb in combinations(range(mins - 1 + len(plts)), len(plts) - 1):
            mspl = []
            prev = -1
            c = 0
            i = 0
            for i, c in enumerate(comb):
                mspl.append(c - prev - 1)
                prev = c
            mspl.append(mins - sum(mspl))

            cop = []
            for s, v in zip(mspl, plts):
                if s == 0:
                    cop.append(v)
                    continue
                by = ceil(v / (s + 1))
                while v >= by:
                    cop.append(by)
                    v -= by
                if v > 0:
                    cop.append(v)
            time = mins + max(cop)
            if time < best:
                best = time
                bestd = cop

    return best

with open(sys.argv[1]) as f:
    for i, line in enumerate(f.readlines()[2::2]):
        plts = [int(x) for x in line.split()]
        res = solve(plts)
        print("Case #%d: %d" % (i + 1, res))
