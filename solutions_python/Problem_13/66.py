#!/usr/bin/python

import sys


def read_string():
    return sys.stdin.readline().strip()

def read_int():
    return int( read_string() )

def read_int_list():
    return [ int( x ) for x in read_string().split() ]


def tree_value( gates, values ):
    M = len( values ) 
    for m in range( (M-1)/2 - 1, -1, -1 ):
        if gates[ m ]:
            values[ m ] = values[ 2*m+1 ] and values[ 2*m + 2 ]
        else:
            values[ m ] = values[ 2*m+1 ] or values[ 2*m + 2 ]
    return values[ 0 ]
    

N = read_int()

for n in range( N ):

    M, V = read_int_list()

    gates = []
    changeable = []
    values = [ None ]*( (M-1)/2 )
    for m in range( (M-1)/2 ):
        G, C = read_int_list()
        gates.append( bool( G ) )
        if C:
            changeable.append( m )
    for m in range( (M+1)/2 ):
        I = read_int()
        values.append( bool( I ) )

    #print gates
    #print changeable
    #print values
    
    solution = len( changeable ) + 1

    for cc in range( 2**len( changeable ) ):
        flipgates = gates[ : ]
        bit = 1
        flip_count = 0
        for offset in range( len( changeable ) ):
            if cc & bit:
                flipgates[ changeable[ offset ] ] = not flipgates[ changeable[ offset ] ]
                flip_count += 1
            bit <<= 1
        #print flip_count, flipgates, tree_value( flipgates, values )
        if tree_value( flipgates, values ) == V:
            if flip_count < solution:
                solution = flip_count

    print 'Case #%i:' % ( n + 1 ),

    if solution <= len( changeable ):
        print solution
    else:
        print 'IMPOSSIBLE'
