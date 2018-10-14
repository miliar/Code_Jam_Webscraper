#!/usr/bin/python
# -*- coding: Shift_JIS -*-

import os, sys, re, math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

c = int(sys.stdin.readline())
for i in range(c):
    t = map(int, sys.stdin.readline().split(' ')[1:])
    t.sort()
    g = t[1] - t[0]
    for j in range(1, len(t) - 1):
        g = gcd(g, t[j + 1] - t[j])
    g = (g * (t[0] / g + 1) - t[0]) % g
    print "Case #" + str(i + 1) + ": " + str(g)
