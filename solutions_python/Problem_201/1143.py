#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Uses https://github.com/rkistner/contest-algorithms

from __future__ import print_function
from heapq import heappush, heappop
import sys

def debug(*args):
    print(*args, file=sys.stderr)

fin = sys.stdin
T = int(fin.readline())
for case in range(1, T + 1):
    n, k = map(int, fin.readline().split())
    debug(n, k)

    q = []
    heappush(q, -n)
    lasta = 0
    lastb = 0
    for i in range(k):
        largest = -heappop(q)
        a = (largest - 1) // 2
        b = largest - 1 - a
        heappush(q, -a)
        heappush(q, -b)
        lasta = a
        lastb = b

    print("Case #%d: %d %d" % (case, lastb, lasta))
    