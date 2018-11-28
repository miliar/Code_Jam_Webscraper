import sys

X = 'X'
O = 'O'
T = 'T'
EMPTY = '.'

X_WON = 'X won'
O_WON = 'O won'
DRAW = 'Draw'
INCOMPLETE = 'Game has not completed'


def getline():
    return sys.stdin.readline().strip()


def traverse4(board, row, col, drow, dcol):
    for _ in xrange(4):
        yield board[row][col]
        row += drow
        col += dcol


def find_winner_in_line(line):
    matching = None

    for c in line:
        if c == EMPTY:
            return None
        elif c == T:
            continue
        elif matching is None or matching == c:
            matching = c
        else:
            return None

    if matching == X:
        return X_WON
    else:
        return O_WON


def find_winner_in_board(board):
    # Analyze columns
    for row_num in xrange(4):
        winner = find_winner_in_line(traverse4(board, row_num, 0, 0, 1))
        if winner is not None:
            return winner

    # Analyze rows
    for col_num in xrange(4):
        winner = find_winner_in_line(traverse4(board, 0, col_num, 1, 0))
        if winner is not None:
            return winner

    # Analyze diagonals
    for args in [(0, 0, 1, 1), (0, 3, 1, -1), (3, 3, -1, -1),
                 (3, 0, -1, 1)]:
        winner = find_winner_in_line(traverse4(board, *args))
        if winner is not None:
            return winner


num_cases = int(getline())

for case in xrange(num_cases):
    EMPTY_EXIST = False

    # Read in board
    board = []
    for _ in xrange(4):
        row = []
        for c in getline():
            if c == EMPTY:
                EMPTY_EXIST = True
            row.append(c)
        board.append(row)
    getline()

    winner = find_winner_in_board(board)
    if winner:
        result = winner
    elif EMPTY_EXIST:
        result = INCOMPLETE
    else:
        result = DRAW

    print "Case #{case}: {result}".format(case=case + 1, result=result)
