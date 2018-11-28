'''Qualification Round Problem A. Speaking in Tongues'''

import sys


SIZE = 4


def checkLine( line ):
    o = 0
    x = 0
    for cell in line:
        if cell == 'O':
            o += 1
        elif cell == 'X':
            x += 1
        elif cell == '.':
            return None

    if o == 0:
        return 'X won'
    elif x == 0:
        return 'O won'
    else:
        return None


def checkResult( board ):
    # horizontal
    for line in board:
        result = checkLine( line )
        if result is not None:
            return result

    # vertical
    for i in range( SIZE ):
        line = ( row[ i ] for row in board )
        result = checkLine( line )
        if result is not None:
            return result

    # diagonal
    line = ( row[ i ] for i, row in enumerate( board ) )
    result = checkLine( line )
    if result is not None:
        return result
    line = ( row[ SIZE - i - 1 ] for i, row in enumerate( board ) )
    result = checkLine( line )
    if result is not None:
        return result

    # completion-check
    for line in board:
        if line.find( '.' ) >= 0:
            return 'Game has not completed'

    return 'Draw'


def main( input ):
    count = int( input.readline() )
    for index in range( 1, count + 1 ):
        board = []
        for rowIndex in range( SIZE ):
            line = input.readline().strip()
            board.append( line )
        input.readline()

        result = checkResult( board )

        print( 'Case #{}: {}'.format( index, result ) )


main( sys.stdin )


