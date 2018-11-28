import collections
import sys

from math import *


def read_line():
    return sys.stdin.readline().rstrip( '\n' )

def read_integer( base = 10 ):
    return int( read_line(), base )

def read_integers( base = 10 ):
    return [ int( x, base ) for x in read_line().split() ]

def read_float():
    return float( read_line() )

def read_floats():
    return [ float( x ) for x in read_line().split() ]

def read_string():
    return read_line().strip()

def read_words():
    return read_line().split()

    

T = read_integer()
for t in range( T ):
    print 'Case #%i:' % ( t + 1 ),
    N, P = read_integers()
    R = read_integers()
    Q = []
    for n in range( N ):
        ingredient = []
        for q in sorted( read_integers() ):
            low = int( ceil( 10*q/( 11*float( R[ n ] ) ) ) )
            high = int( floor( 10*q/( 9*float( R[ n ] ) ) ) )
            if high >= low:
                ingredient.append( ( low, high ) )
        Q.append( sorted( ingredient ) )
    kits = 0
    while all( Q ):
        low = max( q[ -1 ][ 0 ] for q in Q )
        high = min( q[ -1 ][ 1 ] for q in Q )
        if low <= high:
            kits += 1
            for q in Q:
                q.pop()
        else:
            for q in Q:
                if q[ -1 ][ 0 ] == low:
                    q.pop()
    print kits
