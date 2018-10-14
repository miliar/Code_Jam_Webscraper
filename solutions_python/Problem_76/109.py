#!/usr/bin/env python3.2

import functools
import operator
import sys

def readline():
    return next(sys.stdin).strip()

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
    return f

def subsets(s):
    if len(s) == 1:
        yield s, []
        return
    head, rest = s[0], s[1:]
    for in_, out in subsets(rest):
        yield in_, out + [head]
        yield in_ + [head], out

def xor(s):
    return functools.reduce(operator.xor, s, 0)
        
ncases = int(readline())
for caseno in range(ncases):
    _ = readvals(int)
    costs = list(readvals(int))
    if xor(costs) == 0:
        best = sum(costs) - min(costs)
    else:
        best = -1
    print('Case #{}: {}'.format(caseno + 1, best if best is not -1 else 'NO'))
    sys.stdout.flush()
