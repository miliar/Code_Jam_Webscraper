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

def process(x, s, r, t, ww):
    ww = sorted((speed, e - b)  for b, e, speed in ww)
    ww.insert(0, (0, x - sum(d for _, d in ww)))
    time = 0
    for i, (speed, length) in enumerate(ww):
        runspeed = speed + r
        dist = runspeed * t
        if dist < length:
            time += dist / runspeed
            time += (length - dist) / (speed + s)
            break
        needed = length / runspeed
        t -= needed
        time += needed
    for speed, length in ww[i + 1:]:
        time += length / (speed + s)
    return time

ncases = int(readline())
with open(fname + '.out', 'w') as out:
    for caseno in range(ncases):
        x, s, r, t, n  = readvals(int)
        ww = [readvals(int) for _ in range(n)]
        res = process(x, s, r, t, ww)
        print >> out, 'Case #{}: {:f}'.format(caseno + 1, res)
        print 'Case #{}: {:f}'.format(caseno + 1, res)
        sys.stdout.flush()
