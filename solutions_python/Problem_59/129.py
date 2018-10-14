#!/usr/bin/env python2.6

import sys, math
import fractions
from itertools import repeat, count, cycle, ifilter, ifilterfalse, \
                      imap, starmap, tee, izip, product, combinations, \
                      permutations
from collections import defaultdict
from operator import itemgetter


def mapInstance( foo, istream ):
    N, M = map( int, istream.readline().split() )
    idata = []
    for i in xrange(N):
        idata.append( istream.readline().strip() )
    idata2 = []
    for i in xrange(M):
        idata2.append( istream.readline().strip() )
    return foo( idata, idata2 )
    
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

class FS:
    def __init__(self, paths):
        self.root = {}
        self.inserts(paths)

    def splitPath(self, p):
        return p.strip('/').split('/')

    def inserts(self, paths):
        paths.sort()
        cnt = 0
        for p in paths:
            cnt += self.insert(p)
        return cnt

    def insert(self, path):
        path = self.splitPath(path)
        cnt = 0
        n = self.root
        for d in path:
            if d not in n:
                n[d] = {}
                cnt += 1
            n = n[d]
        return cnt


def solve( old, new ):
    fs = FS(old)
    return str(fs.inserts(new))
    
def main( args ):
    mapInput( solve )

if __name__ == "__main__":
    main( sys.argv )
