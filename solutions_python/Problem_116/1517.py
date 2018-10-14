import sys


def solve(board):
    '''
    Read a game board and return the current result.

    Return value will be one of:
        "X won" (the game is over, and X won)
        "O won" (the game is over, and O won)
        "Draw" (the game is over, and it ended in a draw)
        "Game has not completed" (the game is not over yet)
    '''
    rows = board
    cols = [list(X) for X in zip(*rows)]
    diags = diagonalize(rows)

    # Check the whole board, terminate and return
    # if streaks of 4 are encountered
    empty = 0
    for x in (rows + cols + diags):
        T = x.count('T')
        O = x.count('O') + T
        X = x.count('X') + T
        empty += x.count('.')

        if  X == 4:
            return "X won"
        elif  O == 4:
            return "O won"

    # If no one has one, check how many spaces are empty
    if empty == 0:
        return "Draw"
    else:
        return "Game has not completed"

def diagonalize(rows):
    diag = [rows[i][i] for i in range(0,4)]
    anti = [rows[i][3-i] for i in range(0,4)]
    return [diag, anti]


if __name__ == '__main__':

    if len(sys.argv) != 2:
        exit("Error: not enough arguments - specify an input file.")
    f = sys.argv[1]

    fin = open(f)
    fout = open(f[:f.find('.')] + '.out', 'w')
    T = int(fin.readline())


    for i in range(1, T + 1):
        board = [list(fin.readline().strip()) for _ in range(0,4)]
        fin.readline() # consume extra newline
        result = solve(board)
        fout.write("Case #%d: %s\n" % (i, result))