#!/usr/bin/env python

import sys
import re

lines = sys.stdin.readlines()
lines = lines[1:]
num = 0
for line in lines[1::2]:
    num += 1
    a = map(int, line.split(" "))

    """
    n = 0
    for i in range(0, len(a)):
        if a[i] == i+1: continue
        n += 2
        idx = a.index(i+1)
        tmp = a[i]
        a[i] = i+1
        a[idx] = tmp
    """
    n = 0
    for i in range(0, len(a)):
        if a[i] == i+1: continue
        n += 1    

    print >>sys.stdout, "Case #%d: %6f" % (num, n)

