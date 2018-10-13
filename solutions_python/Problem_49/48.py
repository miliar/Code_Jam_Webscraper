#!/usr/bin/env python

import math
import pdb
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


def size(p1, p2):
    x1, y1, r1 = p1
    x2, y2, r2 = p2
    xd = abs(x2-x1)
    yd = abs(y2-y1)
    return math.sqrt(xd*xd+yd*yd)/2.0 + (r1 + r2)/2.0

def best_size(plants):
    bs = 0
    for i in xrange(len(plants)):
        for j in xrange(i, len(plants)):
            bs = max(size(plants[i], plants[j]), bs)
    return bs

def test():
    assert 0 == 0
    import pdb
    #pdb.set_trace()
    assert size((20, 10, 2), (20, 20, 2)) == 7.0
    assert(best_size([(20, 20, 2), (20, 10, 2)]) == 7.0)
    
#    assert(best_size([(40, 10, 3), (20, 10, 2)]) == 7.0)

test()



def do_trial(f):
    plant_count = int(f.readline())
    plants = []
    for i in xrange(plant_count):
        plants.append(list(int(x) for x in f.readline().split()))
    best = 1e20
    for i in xrange(2**plant_count):
        ps1, ps2 = [], []
        #print "---"
        for j, p in enumerate(plants):
            #print i, j, not not(i& (1<<j))
            if i & (1<<j):
                ps1.append(p)
            else:
                ps2.append(p)
        #if len(ps1) < 1 or len(ps2) < 1: continue
        #print ps1, best_size(ps1)
        #print ps2, best_size(ps2)
        best = min(best, max(best_size(ps1), best_size(ps2)))
    return best

f = sys.stdin
#f = file("D-small-attempt0.in.txt")
count = int(f.readline())
for i in xrange(count):
    #pdb.set_trace()
    v = do_trial(f)
    print "Case #%d: %f" % (i+1, v)
