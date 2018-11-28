#!/usr/bin/env python

import sys
from itertools import cycle

def load(stream):
    T = int(stream.readline())
    data = [None]*T
    i = 0
    for t in xrange(T):
        R, k, N = map(int, stream.readline().split())
        g = map(int, stream.readline().split())
        data[i] = (R, k, g)
        i += 1
    return data

def solve(R, k, gs):
    N = len(gs)
    hs = [None]*N
    s = 0
    i = 0
    cnt = 0
    for g in cycle(gs):
        while s+g > k or cnt == N:
            hs[i] = (cnt,s)
            s -= gs[i]
            cnt -= 1
            i += 1
            if i == N: break
        if i == N: break
        s += g
        cnt += 1

    i = 0
    money = 0
    for r in xrange(R):
        cnt, s = hs[i]
        i = (i+cnt)%N
        money += s
    return money


def main():
    d = load(sys.stdin)
    for i, inst in enumerate(d):
        R, k, gs = inst
        money = solve(R, k, gs)
        print "Case #%d: %d" % (i+1, money)


main()

