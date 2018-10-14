import sys

def process_file( fin, fout ):
    def get_one_problem():
        board = []
        for l in range(4):
            board.append( fin.readline() )
        fin.readline()
        return board

    num_cases = int( fin.readline() )
    for i in range( num_cases ):
        board = get_one_problem()
        s = solve_one_problem( board )
        fout.write( "Case #%d: %s\n" % (i+1,s) )

def solve_one_problem( board ):
    for r in range(4):
        X, O, T = count_in_row( board, r )
        if X + T > 3:
            return "X won"
        if O + T > 3:
            return "O won"

    for c in range(4):
        X, O, T = count_in_col( board, c )
        if X + T > 3:
            return "X won"
        if O + T > 3:
            return "O won"

    X, O, T = count_in_diagonal_1( board )
    if X + T > 3:
        return "X won"
    if O + T > 3:
        return "O won"

    X, O, T = count_in_diagonal_2( board )
    if X + T > 3:
        return "X won"
    if O + T > 3:
        return "O won"


    for row in board:
        if any((c == '.') for c in row):
            return "Game has not completed"

    return "Draw"

def count_in_diagonal_1( board ):
    X = 0
    O = 0
    T = 0
    for r in range(4):
        if board[r][r] == 'X':
            X = X + 1
        if board[r][r] == 'O':
            O = O + 1
        if board[r][r] == 'T':
            T = T + 1
    return (X, O, T)

def count_in_diagonal_2( board ):
    X = 0
    O = 0
    T = 0
    for r in range(4):
        if board[r][3-r] == 'X':
            X = X + 1
        if board[r][3-r] == 'O':
            O = O + 1
        if board[r][3-r] == 'T':
            T = T + 1
    return (X, O, T)

def count_in_row( board, r ):
    return ( board[r].count('X'), board[r].count('O'), board[r].count('T') )

def count_in_col( board, c ):
    X = 0
    O = 0
    T = 0
    for r in range(4):
        if board[r][c] == 'X':
            X = X + 1
        if board[r][c] == 'O':
            O = O + 1
        if board[r][c] == 'T':
            T = T + 1
    return (X, O, T)


process_file( open(sys.argv[1]), open(sys.argv[1].replace("in", "out"), "w") )
