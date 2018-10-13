#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import sys
fh = sys.stdin

cases = int(fh.readline())

def fn(s, k):
    p = 0
    c = 0
    s = list(s)
    while p + k <= len(s):
        if s[p] == '-':
            for i in range(k):
                if s[p + i] == '-':
                    s[p + i] = '+'
                else:
                    s[p + i] = '-'
            c += 1
        else:
            p += 1
    if '-' in s:
        c = 'IMPOSSIBLE'
    return c

for x in range(cases):
    (s, k) = fh.readline().strip().split()
    k = int(k)
    r = fn(s, k)
    print('Case #%d: %s' % (x + 1, r))
