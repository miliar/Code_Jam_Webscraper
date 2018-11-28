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
    N = list( read_string() )
    dip = 1
    while dip < len( N ):
        if N[ dip ] < N[ dip - 1 ]:
            break
        dip += 1
    if dip < len( N ):
        drop = dip - 1
        while drop > 0 and N[ drop - 1 ] == N[ drop ]:
            drop -= 1
        N[ drop + 1 : ] = (  len( N ) - drop - 1 )*[ '9' ]            
        N[ drop ] = str( int( N[ drop ] ) - 1 )
    print ''.join( N ).lstrip( '0' )
        
        
