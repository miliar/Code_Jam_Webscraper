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
    if a>b: a,b = b,a
    if a==0: return b
    return gcf(b%a, a)

@Memoize
def is_winning_position(A, B):
    if A==B:
        print "lose from", A, B
        return 0
    if A<B:
        return is_winning_position(B, A)
    print "checking", A, B
    if B == 0: # or A%B == 0:
        print "win! from", A, B
        return 1
    for k in xrange(A/B, 0, -1):
        print "from", A, B, "trying", A-k*B, B
    for k in xrange(A/B, 0, -1):
        if not is_winning_position(A-k*B, B):
            print "move from", A, B, "to %d %d" % (A-k*B, B), "which is a losing position for the opponent"
            return 1
    print "all moves lose from", A, B
    return 0

def do_trial(A1, A2, B1, B2):
    c = 0
    for A in xrange(A1, A2+1):
        for B in xrange(B1, B2+1):
            if is_winning_position(A, B):
                print "*** WINNING:", A, B
                c = c + 1
            else:
                print "*** LOSING:", A, B
    return c

out = file("out", "w")
f = file("in")

T = int(f.readline()[:-1])
for i in range(T):
    A1, A2, B1, B2 = [int(x) for x in f.readline()[:-1].split()]
    v = do_trial(A1, A2, B1, B2)
    print >>out, "Case #%d: %s" % (i+1, v)
    print "Case #%d: %s" % (i+1, v), "of", "%d" % ((B2-B1+1) * (A2-A1+1))
    out.flush()
