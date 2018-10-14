#!/usr/bin/env python3.2

from collections import defaultdict
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

def process(string, combinations, opposed):
    current = []
    for el in string:
        last = current[-1] if current else None
        if (el, last) in combinations:
            current[-1] = combinations[el, last]
        elif opposed[el] & set(current):
            current = []
        else:
            current.append(el)
    return current            

def pprint(elems):
    return '[{}]'.format(', '.join(elems))

ncases = int(readline())
for caseno in range(ncases):
    line = list(readvals(str))
    ncomb = int(line[0])
    combinations = {}
    for a, b, c in line[1:ncomb + 1]:
        combinations[b, a] = c
        combinations[a, b] = c
    opposed = defaultdict(set)
    for a, b in line[ncomb + 2:-2]:
        opposed[a].add(b)
        opposed[b].add(a)
    string = line[-1]
    result = process(string, combinations, opposed)
    print('Case #{}: {}'.format(caseno + 1, pprint(result)))
    sys.stdout.flush()
