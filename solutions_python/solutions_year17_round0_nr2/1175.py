#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Uses https://github.com/rkistner/contest-algorithms

from __future__ import print_function
import sys

def debug(*args):
    print(*args, file=sys.stderr)

fin = sys.stdin
T = int(fin.readline())
for case in range(1, T + 1):
    s = fin.readline().strip()
    si = list(map(int, s))
    n = len(s)
    result = s
    for i, k in enumerate(si):
        ns = str(k) * (n - i)
        if ns > s[i:]:
            result = s[:i] + str(k - 1) + '9' * (n - i - 1)
            break

    if result[0] == '0':
        result = result[1:]
    
    print("Case #%d: %s" % (case, result))
    