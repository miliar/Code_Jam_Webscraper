#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import sys
fh = sys.stdin

cases = int(fh.readline())

def fx(n, k):
    k2 = k
    lvl = 0
    while k2:
        k2 = k2 / 2
        lvl += 1
    taken = (2 ** (lvl-1) - 1)
    sib = k - 1- taken
    left = n - taken
    num = 2 ** (lvl - 1)
    p = left / num
    if sib < (left % num):
        p += 1
    # print('taken = %s, sib = %s, left = %s, num = %s, p = %s' % (taken, sib, left, num, p))

    l = (p-1) / 2
    r = p / 2
    return max(l, r), min(l, r)

for c in range(cases):
    (n, k) = map(int, fh.readline().split())
    (a, b) = fx(n, k)
    print('Case #%d: %d %d' % (c + 1, a, b))
