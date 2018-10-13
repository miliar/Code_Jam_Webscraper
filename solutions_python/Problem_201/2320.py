#!/usr/bin/env python
#-*-coding: utf-8 -*-

from math import log, ceil
import sys

def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())

T = readint()

for t in range(T):
    N, K = readarray(int)
    placed = 2 ** int(log(max(1, K - 1), 2))
    d = int(log(K, 2))
    a = (N - placed) / (2 ** d)
    reste = (N - placed) % (2 ** d)
    if K - placed <= reste:
        a += 1
    a = a - 1
    print "Case #%d: %d %d" % (t + 1, a / 2 + a % 2, a / 2)
