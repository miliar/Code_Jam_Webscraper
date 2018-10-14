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

def do_trial(R, k, groups):
    initial_groups = groups
    money = 0
    while R >= 1:
        R = R - 1
        seats_left = k
        riders = []
        while len(groups) > 0 and seats_left >= groups[0]:
            seats_left -= groups[0]
            riders.append(groups[0])
            groups = groups[1:]
        #print riders
        money = money + sum(riders)
        groups = tuple(list(groups) + riders)
    return money

f = file("C-small-attempt0.in.txt")
T = int(f.readline()[:-1])
for i in range(T):
    R, k, N = [int(x) for x in f.readline()[:-1].split()]
    groups = tuple([int(x) for x in f.readline()[:-1].split()])
    v = do_trial(R, k, groups)
    print "Case #%d: %s" % (i+1, v)
