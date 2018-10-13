'''Online Round 2 Problem A. '''

import sys


def solveold( n, vines, dist ):
    p = 0
    index = 0

    while True:
        d, l = vines[ index ]
        reach = min( d - p, l ) + d
        if reach >= dist:
            return True

        next = -1
        for i in range( index + 1, n ):
            td, tl = vines[ i ]
            if td > reach:
                break
            tr = min( td - d, tl )
            if tr >= next:
                index = i
                next = tr
        if next < 0:
            return False

        p = d

    return True


def solve( cache, n, vines, dist, p = 0, index = 0 ):
    try:
        return cache[ ( p, index ) ]
    except KeyError:
        pass

    d, l = vines[ index ]
    reach = min( d - p, l ) + d
    if reach >= dist:
        cache[ ( p, index ) ] = True
        return True

    next = -1
    for i in range( index + 1, n ):
        td, tl = vines[ i ]
        if td > reach:
            break
        result = solve( cache, n, vines, dist, d, i )
        if result:
            cache[ ( p, index ) ] = True
            return True

    cache[ ( p, index ) ] = False
    return False


def main( input ):
    for index in range( int( input.readline() ) ):
        n, = tuple( map( int, input.readline().replace( '\n', '' ).split() ) )
        vines = []
        for i in range( n ):
            d, l = tuple( map( int, input.readline().replace( '\n', '' ).split() ) )
            vines.append( ( d, l ) )
        dist, = tuple( map( int, input.readline().replace( '\n', '' ).split() ) )

        result = solve( {}, n, vines, dist )

        print( 'Case #{}: {}'.format( index + 1, 'YES' if result else 'NO' ) )


main( sys.stdin )
#main( open( 'D:/Works/codejam/2012/A-small-attempt0.in' ) )
#main( open( 'D:/Works/codejam/2012/input.txt' ) )
