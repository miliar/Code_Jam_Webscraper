#! /usr/bin/env python3

import sys

def solve(shns):
    up = shns[0]
    ret = 0
    for i, x in enumerate(shns[1:]):
        if x == 0:
            continue
        th = i + 1
        if th > up:
            add = th - up
            ret += add
            up += add
        up += x
    return ret

with open(sys.argv[1]) as f:
    for i, line in enumerate(f.readlines()[1:]):
        shns = [int(x) for x in line.split()[1]]
        res = solve(shns)
        print("Case #%d: %d" % (i + 1, res))
