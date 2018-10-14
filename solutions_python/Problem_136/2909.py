#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def debug(a): sys.stderr.write(str(a) + '\n')
def readarray(foo): return [foo(e) for e in input().split()]
def readint(): return int(input().strip())

debug = lambda x: None

def trend(n, C, F, X):
    return F * X - 2 * C -n * C * F - C * F

def total(n, C, F, X):
    result = X / (2 + n * F)
    for i in range(n):
        result += C / (2 + i * F)
    return result

def fastest(C, F, X):
    n = 0
    while trend(n, C, F, X) >= 0:
        debug(trend(n, C, F, X))
        n += 1

    return total(n, C, F, X)

T = readint()
for i in range(T):
    nums = readarray(float)
    debug(nums)
    print('Case #{0}: {1:.7f}'.format(i + 1, fastest(*nums)))
