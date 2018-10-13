#!/usr/bin/env python

import collections

import math
import re
import sys

#sys.setrecursionlimit(50)

INPUT = "tiny"
INPUT = "A-large.in"
#INPUT = "A-small-attempt0.in"


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


def flip(s):
    s1 = ''
    for c in s:
        s1 += '-' if c == '+' else "+"
    return s1


def do_trial(s, c):
    flips = 0
    while len(s) >= c:
        if s[0] == '+':
            s = s[1:]
            continue
        s = flip(s[:c]) + s[c:]
        flips += 1
    if '-' in s:
        return 'IMPOSSIBLE'
    return flips


f = file(INPUT)
T = int(f.readline()[:-1])
for i in range(T):
    s, t = f.readline().split()
    v = do_trial(s, int(t))
    print "Case #%d: %s" % (i+1, v)
