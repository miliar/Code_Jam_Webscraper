#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def debug(*args):
    print(*args, file=sys.stderr)

fin = sys.stdin
T = int(fin.readline())
for case in range(1, T + 1):
    C, F, X = map(float, fin.readline().split())
    # C = cost of buying a candy farm
    # F = number of candies that the farm produces per s
    # X = goal number of candies

    tt = [X/2]
    tt.append(C / 2 + X / (2+F))

    i = 2
    while (tt[-1] <= tt[-2]):
        tt.append(tt[-1] - (X - C) / (2 + F*(i-1)) + X / (2 + F * i))
        i += 1
    result = tt[-2]

    debug(tt)
    print("Case #%d: %s" % (case, result))

