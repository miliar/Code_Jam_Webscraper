#!/usr/bin/env pypy

from __future__ import division

import os.path
import sys

fname, ext = os.path.splitext(sys.argv[0])

try:
    input = open(fname + '.in')
except IOError:
    input = sys.stdin

def readline():
    return next(input).strip()

def readvals(t):
    return map(t, readline().split())

def memoize(func):
    cache = {}
    def f(*args, **kw):
        key = func.__module__, func.__name__, args
        if kw:
            key += frozenset(kw.iteritems()),
        try:
            return cache[key]
        except KeyError:
            cache[key] = result = func(*args, **kw)
            return result
    f.cache = cache
    return f

def process(positions, d):
    p0, v0 = positions[0]
    lastmove = (v0 - 1) * d / 2
    lastpos = p0
    maxmove = lastmove
    for p, v in positions[1:]:
        if lastpos + lastmove + d > p - lastmove:
            # we need to go right first
            start_move = lastmove + (lastpos + d - p) / 2
        else:
            start_move = 0
        lastmove = start_move + (v - 1) * d / 2
        lastpos = p
        maxmove = max(maxmove, lastmove)
    return maxmove

ncases = int(readline())
with open(fname + '.out', 'w') as out:
    for caseno in range(ncases):
        c, d = readvals(int)
        positions = []
        for _ in range(c):
            p, v = readvals(int)
            positions.append((p, v))
        res = process(positions, d)
        print >> out, 'Case #{}: {:f}'.format(caseno + 1, res)
        print 'Case #{}: {:f}'.format(caseno + 1, res)
        sys.stdout.flush()
