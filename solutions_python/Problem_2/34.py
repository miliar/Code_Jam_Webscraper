#!/usr/bin/env python2.5

import sys


def input_text():
    return sys.stdin.readline().strip()

def input_int():
    return int( input_text() )

def input_int_list():
    return ( int( x ) for x in input_text().split() )


def minutes( s ):
    hours, minutes = ( int( x ) for x in s.split( ':' ) )
    return 60*hours + minutes


def travel( journey, start_buffer, start_trains, end_trains ):
    for i, train_ready in enumerate( start_trains ):
        if train_ready <= journey[ 0 ]:
            del start_trains[ i ]
            break
    else:
        start_buffer += 1
    end_trains.append( journey[ 1 ] + T )
    return start_buffer


N = input_int()

for n in range( N ):
    T = input_int()
    NA, NB = input_int_list()
    A_to_B = []
    for na in range( NA ):
        A_to_B.append( [ minutes( s ) for s in input_text().split() ] )
    A_to_B.sort()
    B_to_A = []
    for nb in range( NB ):
        B_to_A.append( [ minutes( s ) for s in input_text().split() ] )
    B_to_A.sort()
    A_to_B.append( [ 1e6 ] )
    B_to_A.append( [ 1e6 ] )

    A_start = 0
    B_start = 0
    A_trains = []
    B_trains = []
    while len( A_to_B ) > 1 or len( B_to_A ) > 1:
        if A_to_B[ 0 ][ 0 ] <= B_to_A[ 0 ][ 0 ]:
            A_start = travel( A_to_B.pop( 0 ), A_start, A_trains, B_trains )
        else:
            B_start = travel( B_to_A.pop( 0 ), B_start, B_trains, A_trains )

    print 'Case #%i: %i %i' % ( n + 1, A_start, B_start )
