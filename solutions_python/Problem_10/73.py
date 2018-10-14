#!/usr/bin/env python

import math, sys

def log( msg ):
    print >>sys.stderr, msg

def intList( stream ):
    return [ int(y) for y in stream.readline().split() ]

def solve( p, k, l, counts ):
    counts.sort()
    counts.reverse()
    result = 0
    for i, c in enumerate( counts ):
        result += c * ( ( i / k ) + 1 )

    return result

stream = sys.stdin
N = int( stream.readline() )
log( "%d test cases" % N )
for i in range( N ):
    p, k, l = intList( stream )
    counts = intList( stream )
    print "Case #%d: %d" % ( i+1, solve( p, k, l, counts ) )
