#!env python2

from __future__ import print_function
import sys
import math

def checkp(n):
    c = str(n)
    l = len(c)
    for i in range(l / 2 + 1):
        if c[i] != c[l - 1 - i]: return False
    return True

def solve(a, b):
    result = []
    l = int(math.sqrt(a))
    r = int(math.sqrt(b))
    if l * l < a: l += 1
    for i in range(l, r + 1):
        if checkp(i) and checkp(i * i):
            result.append(i * i)
    return result

cache = solve(1, 10 ** 14)

n = int(sys.stdin.readline().strip())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    n = len([1 for x in cache if a <= x and x <= b])
    print("Case #%d: %d" % (i + 1, n))
