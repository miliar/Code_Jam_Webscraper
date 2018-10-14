#!/usr/bin/env python2.5

import sys

def input_text():
    return sys.stdin.readline().strip()

def input_int():
    return int( input_text() )

N = input_int()

for n in range( N ):
    S = input_int()
    engines = []
    for s in range( S ):
        engines.append( input_text() )
    Q = input_int()
    queries = []
    for q in range( Q ):
        queries.append( input_text() )
    switches = 0
    engines_left = engines[ : ]
    for q in queries:
        if q in engines_left:
            engines_left.remove( q )
        if not engines_left:
            switches += 1
            engines_left = engines[ : ]
            engines_left.remove( q )
    print 'Case #%i: %i' % ( n + 1, switches )
