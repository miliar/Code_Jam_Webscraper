#!/usr/bin/env python2.5
# encoding: utf-8

import sys, os, re
from bisect import insort
from collections import defaultdict
from functools import wraps, partial
from heapq import heapify, heappush, heappop
from itertools import chain, count, cycle, dropwhile, groupby, ifilter, ifilterfalse, imap, islice, izip, repeat, starmap, takewhile, tee
from operator import lt, le, eq, ne, ge, gt
from operator import add, div, floordiv, mod, mul, neg, sub
from operator import lshift, rshift, invert, and_, or_, xor
from operator import concat, contains, countOf, delitem, delslice, getitem, getslice, indexOf, repeat, setitem, setslice
from operator import attrgetter, itemgetter
from pickle import dumps
from StringIO import StringIO
# http://oakwinter.com/code/functional/
from functional import compose, flip, foldl, foldr, scanl, scanr
# http://probstat.sourceforge.net/
from probstat import Combination, Permutation, Cartesian, PQueue

def debug(f):
    @wraps(f)
    def g(*args, **kwds):
        a = map(repr,args) + map("%s=%r".__rmod__,kwds.items())
        print ">>> %s(%s)" % (f.__name__, ", ".join(a))
        result = f(*args, **kwds)
        if result!=None: print repr(result) 
        return result
    return g
    
INF = float('inf')

#=============================================================================

example = """\
2
3 2 6
8 2 5 2 4 9
3 9 26
1 1 1 100 100 1 1 1 1 1 1 1 1 1 1 1 1 10 11 11 11 11 1 1 1 100
"""

expected = """\
Case #1: 47
Case #2: 397
"""

def parse(inp):
    def next(): return inp.readline().rstrip()
    P, K, L = map(int, next().split())
    freqs = map(int,next().split())
    return P,K,L,freqs
    
@debug
def problem(P, K, L,freqs):
    if L > P*K:
        return "Impossible"
    freqs.sort(reverse=True)
    result = 0
    presses = 1
    for i in range(0,L,K):
        result += sum(freqs[i:i+K]) * presses
        presses += 1
    return result

def format(case, result): 
    return "Case #%d: %s\n" % (case, result)

#=============================================================================

def main(inp, outs):
    def write(s): 
        map(lambda o: o.write(s), outs)
    for case in range(1, int(inp.readline())+1):
        write(format(case, problem(*parse(inp))))
    assert not inp.read()
    
def test():
    import doctest    
    doctest.testmod()
    out = StringIO()
    main(StringIO(example), (out,))
    assert out.getvalue() == expected

if __name__ == '__main__':
    test()
    if len(sys.argv) > 1:
        path = sys.argv[1]
        inp = open(path)
        out = open(os.path.splitext(path)[0] + '.out', 'w')
        main(inp, (out, sys.stdout))
