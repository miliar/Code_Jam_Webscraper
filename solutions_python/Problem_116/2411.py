def read_board():
    board = [raw_input(), raw_input(), raw_input(), raw_input()]
    raw_input()
    return board


def check_verticals(board):
    #print 'Checking verticals'
    cols = []
    for col in xrange(len(board)):
        cols.append([board[0][col], board[1][col], board[2][col], board[3][col]])

    return check_lines(cols)


def check_horizontals(board):
    #print 'Checking horizontals'
    return check_lines(board)


def check_diagonals(board):
    #print 'Checking diagonals'
    diagonals = []
    diagonals.append([board[0][0], board[1][1], board[2][2], board[3][3]])
    diagonals.append([board[3][0], board[2][1], board[1][2], board[0][3]])

    return check_lines(diagonals)


def check_tie (board):
    for line in board:
        for char in line:
            if char == '.':
                return False
    return True


def check_lines(lines):

    for line in lines:
        skip = False
        for char in line:
            if char not in ['X','T']:
                #print 'BAD CHAR IS ' + char
                skip = True
                break
        
        #print 'Skip for x = ' + str(skip)
        if not skip:                
            return 'X'

        skip = False
        for char in line:
            if char not in ['O', 'T']:
                skip = True
                break

        if not skip:
            return 'O'

    return None

def main():
    num_test_cases = int(raw_input())

    for x in range(num_test_cases):
        board = read_board()

        winner = check_horizontals(board)
        #print 'Winner after horizontals = ' + winner
        if winner:
            print 'Case #{}: {} won'.format(x+1, winner)
            continue

        winner = check_verticals(board)
        if winner:
            print 'Case #{}: {} won'.format(x+1, winner)
            continue

        winner = check_diagonals(board)
        if winner:
            print 'Case #{}: {} won'.format(x+1, winner)
            continue

        if check_tie(board):
            print 'Case #{}: Draw'.format(x+1)
            continue

        print 'Case #{}: Game has not completed'.format(x+1)

if __name__ == '__main__':
    main()
