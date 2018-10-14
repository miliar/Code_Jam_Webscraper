#!/usr/bin/env python

import operator
import sys

def read_line():
    return sys.stdin.readline().rstrip( '\n' )

def read_integer():
    return int( read_line() )

def read_integers():
    return [ int( x ) for x in read_line().split() ]

T = read_integer()
for t in range( T ):
    N = read_integer()
    C_i = read_integers()
    C_i.sort()
    print 'Case #%i:' % ( t + 1 ),
    if len( C_i ) < 2 or reduce( operator.xor, C_i ):
        print 'NO'
    else:
        print sum( C_i[ 1 : ] )
