#!/usr/bin/python
import sys

# Infinite House of Pancakes

def wait(p):
    return [c - 1 for c in p if c > 1]

def spec(p, n):
    new_p = list(p[:])
    new_p.remove(max(p))
    new_p.append(max(p) - n)
    new_p.append(n)
    return tuple(new_p)

def minmin(p, m, max_m):
    if len(p) == 0 or m > max_m:
        return m
    results = []
    results.append(minmin(wait(p), m + 1, max_m))
    for n in xrange(max(p)/2, max(p)):
        results.append(minmin(spec(p, n), m + 1, max_m))
    return min(results)

lines = [l.rstrip() for l in sys.stdin.readlines()]
for x in xrange(int(lines.pop(0))):
    d, p = int(lines[2*x]), [int(c) for c in lines[2*x+1].split(' ')]
    m = minmin(p, 0, max(p))
    print "Case #%u: %u" % (x + 1, m)
