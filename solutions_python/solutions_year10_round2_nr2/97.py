#!/usr/bin/env python2.6

import sys, math
import fractions
from itertools import repeat, count, cycle, ifilter, ifilterfalse, \
                      imap, starmap, tee, izip, product, combinations, \
                      permutations
from collections import defaultdict
from operator import itemgetter


def mapInstance( foo, istream ):
    N, K, B, T = map( int, istream.readline().split() )
    X = map( int, istream.readline().split() )
    V = map( int, istream.readline().split() )
    return foo(N, K, B, T, X, V)
    
def mapInput( foo, preproc = None, istream = sys.stdin, ostream = sys.stdout ):
    N = map( int, istream.readline().split() )[0]
    if preproc:
        pass
    odata = starmap( mapInstance, repeat( ( foo, istream ), N ) )
    for i, d in enumerate( odata ):
        print >>sys.stderr, "Case #%d" % ( i+1 )
        print >>ostream, "Case #%d: %s" % ( i+1, d )
    
class showfunction:
    def __init__( self, foo ):
        self.foo = foo
        
    def __call__( self, *args ):
        result = self.foo( *args )
        print >>sys.stderr, args, result
        return result

class cachedfunction:
    def __init__( self, foo ):
        self.foo = foo
        self.cache = {}
        
    def __call__( self, *args ):
        if args in self.cache:
            return self.cache[args]
        else:
            result = self.cache[args] = self.foo( *args )
            return result

def solve(N, K, B, T, X, V):
    X = map(lambda x: B-x, X)
    t = map(lambda (x,v): float(x)/v, izip(X,V))

    swaps = 0
    slows = 0
    chick = N-1
    for k in range(K):
        if chick < 0:
            return "IMPOSSIBLE"
        while t[chick] > T:
            slows += 1
            chick -= 1
            if chick < 0:
                return "IMPOSSIBLE"
        swaps += slows
        chick -= 1
    return str(swaps)

def main( args ):
    mapInput( solve )

if __name__ == "__main__":
    main( sys.argv )
