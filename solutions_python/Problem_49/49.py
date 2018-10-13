#!/usr/bin/env python
# coding: utf-8

import sys
import pprint
from string import uppercase
from heapq import heappush, heappop
from math import sqrt

pp = pprint.PrettyPrinter(width=40)

def read_int_line():
    return tuple(int(i) for i in sys.stdin.readline().split())

def radius((x1, y1, r1), (x2, y2, r2), (x3, y3, r3)):
    d4 = sqrt((x1-x2)**2 + (y1-y2)**2) + r1 + r2
    return max(r3, d4 / 2)

def permutate(tpl, idx):
    return tuple(tpl[i] for i in idx)

PERMS = [(0, 1, 2), (2, 0, 1), (1, 2, 0)]

no_cases = input()
for case in xrange(1, no_cases+1):
    case_size = input()
    flowers = [read_int_line() for _ in xrange(case_size)]
    if case_size in (1, 2):
        answer = max(r for x, y, r in flowers)
    elif case_size == 3:
        answer = min(radius(*permutate(flowers, p)) for p in PERMS)
    else:
        answer = -1
    print 'Case #%d: %.6f' % (case, answer)
