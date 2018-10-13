'''Qualification Round Problem B. Lawnmower'''

import sys


def checkRow( lawn, n, m, value, row ):
    for i in range( m ):
        if lawn[ row ][ i ] > value:
            return False
    return True


def checkCol( lawn, n, m, value, col ):
    for i in range( n ):
        if lawn[ i ][ col ] > value:
            return False
    return True


def checkResult( lawn, n, m ):
    for row in range( n ):
        for col in range( m ):
            result = checkRow( lawn, n, m, lawn[ row ][ col ], row )
            if not result:
                result = checkCol( lawn, n, m, lawn[ row ][ col ], col )
                if not result:
                    return 'NO'
    return 'YES'


def main( input ):
    count = int( input.readline() )
    for index in range( 1, count + 1 ):
        n, m = tuple( map( int, input.readline().split( ' ' ) ) )
        lawn = []
        for rowIndex in range( n ):
            row = tuple( map( int, input.readline().split( ' ' ) ) )
            lawn.append( row )

        result = checkResult( lawn, n, m )

        print( 'Case #{}: {}'.format( index, result ) )


main( sys.stdin )


