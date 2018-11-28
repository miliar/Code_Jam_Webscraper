#!/usr/bin/env python
import gc; gc.disable() # No circular garbage

def memoize(f):
    cache = {}
    def g(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return g

@memoize
def count(n, h, ni, hi):
    if ni == len(n):
        return 1
    if hi == len(h):
        return 0

    total = 0
    if n[ni] == h[hi]:
        total += count(n, h, ni+1, hi+1)
    total += count(n, h, ni, hi+1)
    return total

needle = "welcome to code jam"

import sys
sys.setrecursionlimit(10000)
for i in range(int(sys.stdin.readline())):
    print "Case #%d:" % (i+1),
    haystack = sys.stdin.readline().strip()

    c = count(needle, haystack, 0, 0)
    c = "%04d" % c
    print c[-4:]
