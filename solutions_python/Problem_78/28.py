#!/usr/bin/env python

import re
import sys

class Memoize:
    def __init__(self,function):
        self._cache = {}
        self._callable = function
            
    def __call__(self, *args, **kwds):
        cache = self._cache
        key = self._getKey(*args,**kwds)
        try: return cache[key]
        except KeyError:
            cachedValue = cache[key] = self._callable(*args,**kwds)
            return cachedValue
    
    def _getKey(self,*args,**kwds):
        return kwds and (args, ImmutableDict(kwds)) or args    

def gcf(a,b):
    while a!=b and a>0:
        if a>=b: a,b = b,a
        b-=a
    return a

def lt(a, b):
    if a == 0:
        return 0, 1
    g = gcf(a,b)
    return a/g, b/g

def today_possibilities(N, PD):
    pdn, pdd = lt(PD, 100)
    print N/pdd
    for i in range(1, min(1000,N/pdd+1)):
        yield i*pdn, i*pdd

def forever_possible(wins, total, PG):
    if PG == 100:
        return wins == total
    if PG == 0:
        return wins == 0
    return True

def do_trial(N,PD,PG):
    for wins, total in today_possibilities(N, PD):
        if forever_possible(wins, total, PG):
            return "Possible"
    return "Broken"

out = file("out", "w")
f = file("in")

T = int(f.readline()[:-1])
for i in range(T):
    N, PD, PG = [int(x) for x in f.readline()[:-1].split()]
    v = do_trial(N,PD,PG)
    print >>out, "Case #%d: %s" % (i+1, v)
    out.flush()
