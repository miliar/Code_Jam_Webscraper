#!/usr/bin/env python3

import collections

import math
import pdb
import re
import sys

#sys.setrecursionlimit(50)

INPUT = "tiny"
#INPUT = "A-large.in"
INPUT = "A-small-attempt1.in"


def debug(*args):
    print(*args, file=sys.stderr)


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


def do_trial(N, P, G):
    G = collections.Counter((g % P) for g in G)
    if P == 2:
        debug(P, G)
        return G[0] + (G[1] + 1) // 2
    if P == 3:
        m1 = min(G[1], G[2])
        m2 = max(G[1], G[2]) - m1
        debug(P, m1, m2, G)
        return G[0] + m1 + (m2 + 2) // 3
    return 0


def p(f, t):
    return [t(x) for x in f.readline().split()]


f = open(INPUT)
T = int(f.readline()[:-1])
for i in range(T):
    N, P = p(f, int)
    G = p(f, int)
    v = do_trial(N, P, G)
    print("Case #%d: %s" % (i+1, v))
