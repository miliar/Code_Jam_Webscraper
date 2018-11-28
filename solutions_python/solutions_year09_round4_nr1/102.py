#!/usr/bin/env python

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


#sys.exit(1)

def score(rows):
    s = 0
    for i, r in enumerate(rows):
        #print r[i+1:]
        s += sum(r[i+1:])
    return s

def swap_with_next(rows, i):
    r1, r2 = rows[i], rows[i+1]
    for j in xrange(len(r1)-1, -1, -1):
        if r1[j] != r2[j]:
            if r1[j]:
                r = list(rows[:i]) + [r2, r1] + list(rows[i+2:])
                r = tuple(r)
                return r
            return None

def test():
    assert score([[1, 0], [1, 1]]) == 0
    assert score([(0, 0, 1), (1, 0, 0), (0, 1, 0)]) == 1
    assert score([(1, 1, 1, 0), (1, 1, 0, 0), (1, 1, 0, 0), (1, 0, 0, 0)]) == 2
    #print swap_with_next([(1, 0), (1, 1)], 0)
    assert swap_with_next([(1, 0), (1, 1)], 0) == None #((1,1), (1,0))
    assert swap_with_next([(0, 0, 1), (1, 0, 0), (0, 1, 0)], 0) == ((1, 0, 0), (0, 0, 1), (0, 1, 0))
    #pdb.set_trace()
    assert swap_with_next([(0, 0, 1), (1, 0, 0), (0, 1, 0)], 1) == None #((0, 0, 1), (0, 1, 0), (1, 0, 0))
    assert swap_with_next([(0,0,1), (1,0,0), (0,1,0)], 1) == None

test()

def dump(rows):
    return
    for r in rows:
        print r

@Memoize
def best(rows, best_score=1e6):
    if score(rows) == 0:
        #print "***** SCORE 0", rows
        return 0
    scores = []
    for i in xrange(len(rows)-1):
        new_rows = swap_with_next(rows, i)
        if new_rows:
            dump(rows)
            dump(new_rows)
            scores.append(1+best(new_rows))
    return min(scores)

def do_trial(f):
    row_count = int(f.readline())
    rows = []
    for i in xrange(row_count):
        rows.append(tuple([int(x) for x in list(f.readline()[:-1])]))
    rows = tuple(rows)
    #print rows
    count = best(rows)
    return count

f = file("small") #sys.stdin
f = sys.stdin
count = int(f.readline())
for i in xrange(count):
    v = do_trial(f)
    print "Case #%d: %d" % (i+1, v)
