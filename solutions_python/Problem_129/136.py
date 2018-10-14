#!/usr/bin/env python

import collections

import math
import re
import sys

INPUT = "tiny"
if 1: #1:
    INPUT = "A-small-attempt2.in"

def debug(*args):
    #print str(args)
    pass

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

def cost(M, N):
    return M * N + M * (1-M) / 2

assert cost(1, 5) == 5
assert cost(2, 5) == 5 + 4
assert cost(3, 5) == 5 + 4 + 3
assert cost(4, 5) == 5 + 4 + 3 + 2
assert cost(5, 6) == 6 + 5 + 4 + 3 + 2
assert cost(6, 6) == 6 + 5 + 4 + 3 + 2 + 1


def improve(N, array):
    swaps = 0
    for s0 in range(N):
        for e0 in range(s0+1, N):
            #debug("checking %s, %s" % (s0+1, e0+1))
            p0 = array[s0][e0]
            if p0 == 0:
                continue
            #import pdb; pdb.set_trace()
            for e1 in range(N-1, e0, -1):
                for s1 in range(s0+1, e0+1):
                    p1 = array[s1][e1]
                    if p1 == 0: continue
                    swaps = 1
                    smaller = min(p0, p1)
                    debug("swapping (%s %s) with (%s, %s) [%s]" % (s0+1, e0+1, s1+1, e1+1, smaller))
                    p0 -= smaller
                    array[s0][e0] -= smaller
                    array[s1][e1] -= smaller
                    array[s0][e1] += smaller
                    array[s1][e0] += smaller
                    if p0 == 0: break
                if p0 == 0: break
    return swaps

def find_total(N, array):
    total = 0
    for o in range(N):
        for e in range(o+1, N):
            p = array[o][e]
            if p:
                total += cost(e-o, N) * p
                total %= 1000002013
    return total

def show_array(N, array):
    for s0 in range(N):
        for e0 in range(s0, N):
            p0 = array[s0][e0]
            if p0>0:
                debug("%s %s %s" % (s0+1, e0+1, p0))

def do_trial(N, M, triples):
    array = [[0] * N for i in range(N)]
    for (s, e, p) in triples:
        array[s-1][e-1] += p
    original_total = find_total(N, array)
    show_array(N, array)
    while 1:
        c = improve(N, array)
        if not c: break
    show_array(N, array)
    new_total = find_total(N, array)
    #import pdb; pdb.set_trace()
    return (original_total-new_total) % 1000002013

f = file(INPUT)
T = int(f.readline()[:-1])
for i in range(T):
    N, M = [int(x) for x in f.readline().split()]
    debug("**** %s, %s" % (N,M))
    triples = []
    for j in range(M):
        triples.append([int(x) for x in f.readline().split()])
    v = do_trial(N, M, triples)
    print "Case #%d: %s" % (i+1, v)
