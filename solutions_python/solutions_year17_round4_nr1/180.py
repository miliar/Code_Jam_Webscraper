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

def input_string_stack():
    data = []
    for line in sys.stdin.readlines():
        data.extend( line.split() )
    data.reverse()
    return data

def input_integer_stack():
    return [ int( x ) for x in read_string_stack() ]

def bits( x ):
    return bin( x ).count( '1' )

T = read_integer()
for t in range( T ):
    print 'Case #%i:' % ( t + 1 ),
    N, P = read_integers()
    G = read_integers()
    a = collections.Counter()
    for g in G:
        a[ g % P ] += 1
    if P == 2:
        count = a[ 0 ]
        count += ( a[ 1 ] + 1 )//2
    elif P == 3:
        count = a[ 0 ]
        t = min( a[ 2 ], a[ 1 ] )
        count += t
        a[ 2 ] -= t
        a[ 1 ] -= t
        count += a[ 1 ]//3
        a[ 1 ] -= 3*(a[ 1 ]//3)
        count += a[ 2 ]//3
        a[ 2 ] -= 3*(a[ 2 ]//3)
        if a[ 1 ] or a[ 2 ]:
            count += 1
    elif P == 4:
        count = a[ 0 ]
        
        t = min( a[ 1 ], a[ 3 ] )
        a[ 1 ] -= t
        a[ 3 ] -= t
        count += t
        
        t = min( a[ 1 ]//2, a[ 2 ] )
        a[ 1 ] -= 2*t
        a[ 2 ] -= t
        count += t
        
        t = min( a[ 3 ]//2, a[ 2 ] )
        a[ 3 ] -= 2*t
        a[ 2 ] -= t
        count += t
        
        t = a[ 2 ]//2
        a[ 2 ] -= 2*t
        count += t
        
        t = a[ 1 ]//4
        a[ 1 ] -= 4*t
        count += t
        
        t = a[ 3 ]//4
        a[ 3 ] -= 4*t
        count += t
        
        if a[ 1 ] or a[ 2 ] or a[ 3 ]:
            count += 1

        c0 = count

        count = a[ 0 ]
        
        t = min( a[ 1 ], a[ 3 ] )
        a[ 1 ] -= t
        a[ 3 ] -= t
        count += t
        
        t = a[ 2 ]//2
        a[ 2 ] -= 2*t
        count += t
        
        t = min( a[ 1 ]//2, a[ 2 ] )
        a[ 1 ] -= 2*t
        a[ 2 ] -= t
        count += t
        
        t = min( a[ 3 ]//2, a[ 2 ] )
        a[ 3 ] -= 2*t
        a[ 2 ] -= t
        count += t
        
        t = a[ 1 ]//4
        a[ 1 ] -= 4*t
        count += t
        
        t = a[ 3 ]//4
        a[ 3 ] -= 4*t
        count += t
        
        if a[ 1 ] or a[ 2 ] or a[ 3 ]:
            count += 1

        count = max( c0, count )

        count = a[ 0 ]
        
        t = min( a[ 1 ]//2, a[ 2 ] )
        a[ 1 ] -= 2*t
        a[ 2 ] -= t
        count += t
        
        t = min( a[ 3 ]//2, a[ 2 ] )
        a[ 3 ] -= 2*t
        a[ 2 ] -= t
        count += t
        
        t = min( a[ 1 ], a[ 3 ] )
        a[ 1 ] -= t
        a[ 3 ] -= t
        count += t
        
        t = a[ 2 ]//2
        a[ 2 ] -= 2*t
        count += t
        
        t = a[ 1 ]//4
        a[ 1 ] -= 4*t
        count += t
        
        t = a[ 3 ]//4
        a[ 3 ] -= 4*t
        count += t
        
        if a[ 1 ] or a[ 2 ] or a[ 3 ]:
            count += 1

        count = max( c0, count )
    else:
        assert 0
    print count
