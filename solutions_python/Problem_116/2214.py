import re

lines = []
with open('input.txt','r') as f:
    lines = f.read().splitlines()

lines.pop(0)

valid_line = re.compile(r'[XOT\.]{4}')

lines = map(lambda line: line.upper().strip(), lines)
lines = filter(lambda line: valid_line.match(line), lines)

boards = []

assert len(lines) % 4 == 0

chunks = len(lines) / 4

for i in xrange(chunks):
    this_board = []
    for j in xrange(4):
        this_board.append(lines.pop(0))
    boards.append(this_board)

X_WON = 5
O_WON = 6
DRAW  = 7
NOT_FINISHED = 8

X_WON_STATES = ['XXXX','TXXX','XTXX','XXTX','XXXT']
O_WON_STATES = ['OOOO','TOOO','OTOO','OOTO','OOOT']

def get_columns(board):
    columns = []
    for i in xrange(4):
        this_column = ''
        for j in xrange(4):
            this_column += board[j][i]
        columns.append(this_column)
    return columns

def has_empty_spot(board):
    for row in board:
        if '.' in row:
            return True
    return False

def get_diagonals(board):
    first_diagonal  = board[0][0] + board[1][1] + board[2][2] + board[3][3]
    second_diagonal = board[0][3] + board[1][2] + board[2][1] + board[3][0]
    return [first_diagonal, second_diagonal]

def check_rows(board):
    for row in board:
        if row in X_WON_STATES:
            return X_WON
        elif row in O_WON_STATES:
            return O_WON
    return False

def check_columns(board):
    columns = get_columns(board)
    for column in columns:
        if column in X_WON_STATES:
            return X_WON
        elif column in O_WON_STATES:
            return O_WON
    return False

def check_diagonals(board):
    diagonals = get_diagonals(board)
    for diagonal in diagonals:
        if diagonal in X_WON_STATES:
            return X_WON
        elif diagonal in O_WON_STATES:
            return O_WON
    return False

def get_results(status):
    if status == X_WON:
        return 'X won'
    elif status == O_WON:
        return 'O won'
    elif status == DRAW:
        return 'Draw'
    elif status == NOT_FINISHED:
        return 'Game has not completed'
    else:
        return 'NOT RECOGNISED!'

def check_board(board):

    row_status = check_rows(board)
    if row_status in [X_WON, O_WON]:
        return get_results(row_status)

    column_status = check_columns(board)
    if column_status in [X_WON, O_WON]:
        return get_results(column_status)

    diagonal_status = check_diagonals(board)
    if diagonal_status in [X_WON, O_WON]:
        return get_results(diagonal_status)

    if has_empty_spot(board):
        return get_results(NOT_FINISHED)
    else:
        return get_results(DRAW)

out_file = open('output.txt', 'w')

case = 1
for board in boards:
    line = 'Case #%d: %s' % (case, check_board(board))
    #print line
    out_file.write(line + '\n')
    case += 1

out_file.close()
