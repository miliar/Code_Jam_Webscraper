#!/usr/bin/env python3.2

import sys
from collections import Counter

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

def canonical(n):
    if n == 0:
        return 0
    s = str(n)
    return int(min(s[i:] + s[:i] for i in range(len(s)) if s[i] != '0'))

can = [canonical(i) for i in range(2000001)]

ncases = int(readline())
for caseno in range(ncases):
    a, b = readvals(int)
    found = Counter(can[a: b + 1])
#    print([v for v in found.values() if v >= 2])
    print('Case #{}: {}'.format(caseno + 1, sum(n * (n - 1) // 2
                                                for n in found.values())))
    sys.stdout.flush()
