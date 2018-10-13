#!/usr/bin/env python

import sys

def read_int():
    return int( sys.stdin.readline().strip() )

def read_int_list():
    return [ int( x ) for x in sys.stdin.readline().strip().split() ]

T = read_int()

for i in range( T ):

    n = read_int()

    v1 = read_int_list()
    v2 = read_int_list()

    v1.sort()
    v2.sort()

    product = 0
    
    while v1 and v1[ 0 ] <= 0 and v2[ -1 ] >= 0:
        x = v1.pop( 0 )
        y = v2.pop()
        product += x*y
    while v1 and v2[ 0 ] <= 0 and v1[ -1 ] >= 0:
        x = v2.pop( 0 )
        y = v1.pop()
        product += x*y
    v2.reverse()

    while v1:
        product += v1.pop()*v2.pop()

    print 'Case #%i: %i' % ( i + 1, product )

