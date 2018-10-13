import sys
import fileinput

xwon = "X won"
owon = "O won"
draw = "Draw"
incomplete = "Game has not completed"
n = 4

def game_over(board):
    for row in board:
        if '.' in row:
            return False
    return True

def has_match(row):
    if '.' in row:
        return None

    if 'X' in row and 'O' not in row:
        return 'X'
    elif "O" in row and 'X' not in row:
        return 'O'
    else:
        return None

def check_rows(board):
    for row in board:
        match = has_match(row)
        if match is not None:
            return match
    return None

def check_columns(board):
    transpose = map(list, zip(*board))
    return check_rows(transpose)

def check_diagonals(board):
    diag1 = [board[i][i] for i in range(n)]
    diag2 = [board[n-1-i][i] for i in range(n-1,-1, -1)]

    match1 = has_match(diag1)
    match2 = has_match(diag2)
    if match1 is not None:
        return match1
    else:
        return match2

def winner(board):
    rows = check_rows(board)
    if rows is not None:
        return rows
    cols = check_columns(board)
    if cols is not None:
        return cols
    diags = check_diagonals(board)
    if diags is not None:
        return diags


def process(board):
    win = winner(board)
    if win is 'X':
        return xwon
    elif win is 'O':
        return owon
    elif game_over(board):
        return draw
    else:
        return incomplete

def run (input_file, output_file):
    outfile = open(output_file, 'w')

    total_tc = 0
    row = 0
    board = []
    count = 0
    for line in fileinput.input(input_file):
        if fileinput.isfirstline():
            total_tc = int(line)
        elif line == "\n":
            count += 1
            outfile.write("Case #" + str(count) + ": " + process(board)+line)
            board = []
        else:
            board.append(list(line.strip()))

    outfile.close()


if len(sys.argv) < 3:
    print "Usage: python tictactotem <input> <output>"
else:
    run(sys.argv[1], sys.argv[2])
