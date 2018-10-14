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
    print 'Case #%i:' % ( t + 1 )
    R, C = read_integers()
    cake = []
    for r in range( R ):
        cake.append( list( read_string() ) )
    letters = {}
    for r in range( R ):
        for c in range( C ):
            if cake[ r ][ c ] != '?':
                letters[ cake[ r ][ c ] ] = r, c
    for letter in letters:
        r0, c0 = letters[ letter ]
        r = r0 - 1
        c = c0
        while r >= 0 and cake[ r ][ c ] == '?':
            cake[ r ][ c ] = letter
            r -= 1
        r = r0 + 1
        c = c0
        while r < R and cake[ r ][ c ] == '?':
            cake[ r ][ c ] = letter
            r += 1
    c = 0
    while cake[ 0 ][ c ] == '?':
        c += 1
    for cc in range( c ):
        for r in range( R ):
            cake[ r ][ cc ] = cake[ r ][ c ]
    for c in range( c + 1, C ):
        if cake[ 0 ][ c ] == '?':
            for r in range( R ):
                cake[ r ][ c ] = cake[ r ][ c - 1 ]
    print '\n'.join( ''.join( cake[ r ] ) for r in range( R ) )
