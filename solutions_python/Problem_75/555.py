#!/usr/bin/env python

import re
import sys

INPUT = "tiny"
if 1:
    INPUT = "B-small-attempt2.in.txt"

def debug(*args):
    pass
    print >>sys.stderr, str(args)

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

def do_trial(items):
    invokers = {}
    combiners = {}
    idx = 0
    count = int(items[idx])
    idx += 1
    for i in xrange(count):
        ivk = items[idx]
        idx += 1
        invokers[ivk[0:2]] = ivk[-1]
        invokers[''.join(reversed(ivk[0:2]))] = ivk[-1]
    count = int(items[idx])
    idx += 1
    for i in xrange(count):
        a,b = items[idx]
        combiners[a] = b
        combiners[b] = a
        idx +=1 
    idx +=1 
    text = items[idx]
    idx += 1
    debug(invokers)
    result = [] #list(text)
    debug(result)
    for c in text:
        debug("at %s; adding %s" % (''.join(result), c))
        result.append(c)
        if len(result) > 1:
            last_two = ''.join(result[-2:])
            if last_two in invokers:
                result = result[:-2]
                for c in invokers[last_two]:
                    result.append(c)
            if c in combiners:
                if combiners[c] in result:
                    result = []
    return "[%s]" % ", ".join(result)

f = file(INPUT)
T = int(f.readline()[:-1])
for i in range(T):
    items = f.readline()[:-1].split()
    debug(items)
    v = do_trial(items)
    print "Case #%d: %s" % (i+1, v)
