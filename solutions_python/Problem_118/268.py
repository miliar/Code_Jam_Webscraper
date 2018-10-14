#! /usr/local/bin/python
# -*- coding: utf-8 -*-

import math

palin = []

def isPalindrome( number ):

    rev = number[ :: -1 ]

    return rev == number


def addDigit( seed, k ):

    if k > 100:
        return

    new_seed = []
    
    for s in seed:

        for i in range( 10 ):
            x = str( i ) + s + str( i )

            if i == 0:
                new_seed.append( x )
                continue

            if isPalindrome( str( int( x )**2 ) ):
                palin.append( int( x )**2 )
                new_seed.append( x )
            else:
                break

    addDigit( new_seed, k + 2 )


if __name__ == '__main__':

    seed = []

    for i in range( 10 ):
        if i == 0:
            seed.append( str( i ) )
            continue

        if isPalindrome( str( i**2 ) ):
            palin.append( i**2 )
            seed.append( str( i ) )
        else:
            break

    addDigit( seed, 1 )

    seed = []
    for i in range( 10 ):
        if i == 0:
            seed.append( str( i ) * 2 )
            continue

        if isPalindrome( str( ( i * 10 + i )**2 ) ):
            palin.append( ( i * 10 + i )**2 )
            seed.append( str( i ) * 2 )
        else:
            break

    addDigit( seed, 2 )

    test = input()

    for t in range( test ):

        a, b = raw_input().split()
        a = int( a )
        b = int( b )

        print "Case #%d: %d" % ( t + 1, len( [ x for x in palin if x >= a and x <= b ] ) )


