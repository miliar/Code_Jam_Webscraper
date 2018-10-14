#!/usr/bin/env python3.1

import functools
import fractions
import itertools
import sys

def readline():
    return next(sys.stdin).strip()

def readvals(t):
    return map(t, readline().split())

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

C = int(readline())
for i in range(C):
    events = sorted(list(readvals(int))[1:])
    differences = [b - a for a, b in pairwise(events)]
    gcd = functools.reduce(fractions.gcd, differences)
    res = -events[0] % gcd
    
    print('Case #{}: {}'.format(i + 1, res))
