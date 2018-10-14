import sys
def process_board(board):
    transposed = ['','','','']
    for row in board:
        j=0
        for square in row:
            transposed[j] += square
            j+=1

#    for row in board:
#        print row
#    print ''
#    for row in transposed:
#        print row

    board_not_filled = False

    for row in board:
        result = process_row(row)
        if( result == 'empty square'):
            board_not_filled = True
        elif( result == 'O won'):
            return 'O won'
        elif( result == 'X won'):
            return 'X won'

    for row in transposed:
        result = process_row(row)
        if( result == 'O won'):
            return 'O won'
        elif( result == 'X won'):
            return 'X won'

    diag1 = diag2 = ''
    for i in range(4):
        diag1 += board[i][i]
        diag2 += board[i][3 - i]
            
  #  print diag1
  #  print diag2

    result = process_row(diag1)
    if( result == 'O won'):
        return 'O won'
    elif( result == 'X won'):
        return 'X won'

    result = process_row(diag2)
    if( result == 'O won'):
        return 'O won'
    elif( result == 'X won'):
        return 'X won'

    if ( board_not_filled ):
        return "Game has not completed"
    else:
        return "Draw"


def process_row(row):
    if( not (row.find('.') == -1 ) ):
        return 'empty square'
    elif( row.find('X') == -1):
        return 'O won'
    elif( row.find('O') == -1):
        return 'X won'
    return ''

if ( __name__ == '__main__'):
    input = sys.stdin.readlines()
    num_cases = int(input[0])
#    print num_cases, len(input)
    assert ( input[-1] == '\n' )
    i=1
    board = []
    for j in range(1, len(input)):
        if( input[j] == '\n'):
            result = process_board(board)
            print 'Case #%d:' % i, result 
            board = []
            i+=1
        else:
            board.append(input[j].strip('\n'))
