#!/usr/bin/env python

import re
import sys

INPUT = "tiny"
if 1:
    INPUT = "A-large.in.txt"

def debug(*args):
    pass #print str(args)

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

def do_trial(pairs):
    pos = dict({ "B" : 1, "O" : 1 })
    slop = dict({ "B" : 0, "O" : 0 })
    k = 0
    moves = 0
    for col1, z in pairs:
        debug(pos, slop, moves)
        b_pos = int(z)
        debug(col1, b_pos)
        col2 = chr(ord("B") ^ ord("O") ^ ord(col1))
        distance = max(0,abs(pos[col1] - b_pos)-slop[col1]) + 1
        pos[col1] = b_pos
        slop[col1] = 0
        slop[col2] = slop[col2] + distance
        moves += distance
    return moves

f = file(INPUT)
T = int(f.readline()[:-1])
for i in range(T):
    items = f.readline()[:-1].split()[1:]
    pairs = [(items[v],items[v+1]) for v in xrange(0,len(items)-1,2)]
    debug(pairs)
    #N, K = [int(x) for x in f.readline()[:-1].split()]
    v = do_trial(pairs)
    print "Case #%d: %s" % (i+1, v)
