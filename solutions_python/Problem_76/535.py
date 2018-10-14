#!/usr/bin/env python

import re
import sys

INPUT = "tiny"
if 1:
    INPUT = "C-large.in.txt"

def debug(*args):
    pass
    #print >>sys.stderr, str(args)

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

def do_trial(candies):
    t = 0
    for c in candies:
        t ^= c
    if t != 0 or len(candies) < 2:
        return "NO"
    return "%s" % sum(sorted(candies)[1:])

f = file(INPUT)
T = int(f.readline()[:-1])
for i in range(T):
    N = int(f.readline()[:-1])
    items = [int(x) for x in f.readline()[:-1].split()]
    debug(items)
    v = do_trial(items)
    print "Case #%d: %s" % (i+1, v)
