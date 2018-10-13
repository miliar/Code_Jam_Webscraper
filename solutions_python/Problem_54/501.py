#!/usr/bin/env python2.6

import sys
import itertools
import math

def load(stream):
    T = int(stream.readline())
    data = [None]*T
    i = 0
    for t in xrange(T):
        t = map(int, stream.readline().split())
        data[i] = t[1:]
        i += 1
    return data

def gcd(u, v):
    if u == 0:
        return v
    if v == 0:
        return u
 
    shift = 0
    while u & 1 == 0 and v & 1 == 0:
         shift += 1
         u = u >> 1;
         v = v >> 1;
 
    while u & 1 == 0:
        u = u >> 1
 
    while v != 0:
        while v & 1 == 0:
            v = v >> 1;

        if u < v:
            v -= u
        else:
            diff = u-v
            u = v
            v = diff
        v = v >> 1

    return u << shift

def solve(ts):
    ts = list(set(ts))
    ts.sort()
    N = len(ts)
    diffs = map(lambda i: ts[i]-ts[i-1], range(1,N))
    #diffs = map(lambda a: abs(a[0]-a[1]), itertools.combinations(ts,2))
    opt = reduce(gcd, diffs)
    return max(map(lambda x: (opt-(x%opt))%opt, ts))

def main():
    d = load(sys.stdin)
    for i, inst in enumerate(d):
        print >>sys.stderr, "%d" % i
        n = solve(inst)
        print "Case #%d: %d" % (i+1, n)


main()

