#!/usr/bin/env python

import collections
import itertools

import math
import re
import sys

#sys.setrecursionlimit(50)

INPUT = "tiny"
#INPUT = "A-large.in"
INPUT = "B-small-attempt0.in"

def debug(*args):
    return
    sys.stderr.write(str(args) + "\n")

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

def do_trial(A, B, K):
    count = 0
    for a in range(A):
        for b in range(B):
            debug(a, b, a&b, K)
            if a & b < K:
                count += 1
    return count

f = file(INPUT)
T = int(f.readline()[:-1])
for i in range(T):
    A, B, K = [int(x) for x in f.readline().split()]
    v = do_trial(A, B, K)
    print "Case #%d: %s" % (i+1, v)
