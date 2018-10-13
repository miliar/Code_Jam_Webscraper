#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import sys
fh = sys.stdin

cases = int(fh.readline())

def fx(n):
    while True:
        # scan from lsb.
        s = str(n)
        p = len(s) - 1
        while p > 0:
            if s[p] < s[p-1]:
                break
            else:
                p -= 1
        if p == 0: break
        w = len(s) - 1 - p
        chunk = 10 ** w
        n = (n - chunk) / chunk * chunk + chunk - 1
    return n

for c in range(cases):
    n = int(fh.readline())
    r = fx(n)
    print('Case #%d: %d' % (c + 1, r))
