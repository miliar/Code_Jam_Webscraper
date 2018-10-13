#!/usr/bin/env python

import sys

def read_line():
    return sys.stdin.readline().rstrip( '\n' )

def read_integer():
    return int( read_line() )

def read_integers():
    return [ int( x ) for x in read_line().split() ]

def read_strings():
    return read_line().split()

def input_string_stack():
    data = []
    for line in sys.stdin.readlines():
        data.extend( line.split() )
    data.reverse()
    return data

def input_integer_stack():
    return [ int( x ) for x in read_string_stack() ]

def choose( N, k ):
    return factorial[ N ]/( factorial[ k ]*factorial[ N - k ] )

def expected( length ):
    if length <= 1:
        return 0
    way_sum = 0
    weighted_sum = 0
    for correct in range( 1, length + 1 ):
        ways = choose( length, correct )*derangements[ length - correct ]
        if ways:
            steps = 1 + expected( length - correct )
            way_sum += ways
            weighted_sum += ways*steps
    return 1.*( weighted_sum + factorial[ length ] )/way_sum - 1

factorial = [ 1 ]
for n in range( 1, 1001 ):
    factorial.append( n*factorial[ - 1 ] )
derangements = [ 1, 0 ]
for n in range( 2, 1001 ):
    derangements.append( ( n - 1 )*( derangements[ n - 1 ] + derangements[ n - 2 ] ) )
T = read_integer()
for t in range( T ):
    N = read_integer()
    array = read_integers()
    array = [ unordered if unordered != ordered else None for ( unordered, ordered ) in zip( array, sorted( array ) )  ]
    total_steps = 0
    for index in range( len( array ) ):
        if array[ index ] is None:
            continue
        length = 0
        pointer = index + 1
        while array[ pointer - 1 ] is not None:
            array[ pointer - 1 ], pointer = None, array[ pointer - 1 ]
            length += 1
        total_steps += expected( length )
    print 'Case #%i: %0.6f' % ( t + 1, total_steps )


#1 2
#2 1

#1 2 3       1
#1 3 2       1 + 2
#2 1 3       1 + 2
#2 3 1       #
#3 1 2       #
#3 2 1       1 + 2


#x   = 1/6*( 1 + 3 + 3 + (1+x) + (1+x) + 3 )
    #= ( 10 + 2 + 2*x )/6
    #= ( 12 + 2*x )/6
    #= 2 + x/3

#x = 1/6*( 1 + 3 + 3 + 2*(x+1) + 3 )
