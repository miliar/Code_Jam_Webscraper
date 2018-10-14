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

def read_strings():
    return read_line().split()

T = read_integer()
for t in range( T ):
    print 'Case #%i:' % ( t + 1 ),
    S, K = read_strings()
    S = [ s == '+' for s in S ]
    K = int( K )
    flips = 0
    for index in range( len( S ) - K + 1 ):
        if not S[ index ]:
            for flip in range( index, index + K ):
                S[ flip ] = not S[ flip ]
            flips += 1
    for index in range( len( S ) - K + 1, len( S ) ):
        if not S[ index ]:
            print 'IMPOSSIBLE'
            break
    else:
        print flips
