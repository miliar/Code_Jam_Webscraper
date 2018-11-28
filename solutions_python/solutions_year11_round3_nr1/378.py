from codejam import *

def doboard(board):
    R = len(board)
    C = len(board[0])
    for rr in range(R-1):
        while True:
            try:
                cc = board[rr].index('#')
            except ValueError:
                break
            if cc == C-1 or board[rr][cc+1] != '#': return "Impossible"
            if board[rr+1][cc] != '#' or board[rr+1][cc+1] != '#': return "Impossible"
            board[rr][cc] = '/'
            board[rr][cc+1] = '\\'
            board[rr+1][cc] = '\\'
            board[rr+1][cc+1] = '/'
    if '#' in board[-1]: return "Impossible"
    return '\n'.join([''.join(b) for b in board])

@main
def SquareTiles():
    T = read_int()
    for case in range(T):
        R, C = read_ints()
        board = []
        for i in range(R):
            board.append(list(read_str()))
        result = doboard(board)
        printcase(case, result, sep='\n')
