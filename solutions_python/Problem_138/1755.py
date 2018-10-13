#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout

from bisect import bisect_right
from collections import deque


def simple_war(NW, KW):
    NW = NW[:]
    KW = KW[:]
    n_points = 0
    while NW:
        nw = NW.pop()
        k = bisect_right(KW, nw)
        if k == len(KW):
            KW.pop(0)
            n_points += 1
        else:
            KW.pop(k)
    return n_points


def deceitful_war(NW, KW):
    NW = deque(NW)
    KW = deque(KW)
    n_points = 0
    while KW:
        kw = KW.pop()
        if kw > NW[-1]:
            NW.popleft()
        else:
            NW.pop()
            n_points += 1
    return n_points


def solve(NW, KW):
    NW.sort()
    KW.sort()
    #print NW
    #print KW
    sw = simple_war(NW, KW)
    dw = deceitful_war(NW, KW)
    return dw, sw


def numbers_from_line(d=' ', mapf=int):
    return [mapf(s) for s in ifs.readline().strip().split(d)
            if len(s.strip()) > 0]


T = int(ifs.readline())
for t in range(1, T + 1):
    N = int(ifs.readline())
    NW = numbers_from_line(d=' ', mapf=float)
    KW = numbers_from_line(d=' ', mapf=float)
    assert len(NW) == len(KW) and len(KW) == N
    dw, w = solve(NW, KW)
    ofs.write('Case #%d: %d %d\n' % (t, dw, w))
