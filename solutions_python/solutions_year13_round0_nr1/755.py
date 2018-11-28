import sys

NUM_ROWS = 4
NUM_COLS = 4
X_WIN = ['X'] * 4
O_WIN = ['O'] * 4

num_cases = int(sys.stdin.readline())

def test_winner(line):
    if line == X_WIN:
        return 'X won'
    elif line == O_WIN:
        return 'O won'
    else:
        return None

def read_board():
    board = [list(sys.stdin.readline().strip()) for _ in xrange(NUM_ROWS)]
    sys.stdin.readline()

    board_lines = list(board)
    for j in xrange(NUM_COLS):
        board_lines.append([board[i][j] for i in xrange(NUM_ROWS)])
    board_lines.append([board[i][i] for i in xrange(NUM_ROWS)])
    board_lines.append([board[i][-(i+1)] for i in xrange(NUM_ROWS)])

    complete = True
    for line in board_lines:
        if '.' in line:
            complete = False
        if 'T' in line:
            T_index = line.index('T')
            X_line = list(line)
            X_line[T_index] = 'X'
            O_line = list(line)
            O_line[T_index] = 'O'
            res = test_winner(X_line)
            if res:
                return res
            res = test_winner(O_line)
            if res:
                return res
        else:
            res = test_winner(line)
            if res:
                return res
    if complete:
        return 'Draw'
    else:
        return 'Game has not completed'

for j in xrange(num_cases):
    print "Case #%s: %s" % (j+1, read_board())
    j += 1
