import sys

def winner(fields):
    w = set(fields).difference(set('T'))
    if len(w) == 1:
        r = w.pop()
        if r != '.':
           return r 

def rows(board):
    for i in xrange(4):
        yield list(board[i])

def columns(board):
    for i in xrange(4):
        yield [board[0][i], board[1][i], board[2][i], board[3][i]] 

def diagonals(board):
    yield [board[0][0], board[1][1], board[2][2], board[3][3]] 
    yield [board[0][3], board[1][2], board[2][1], board[3][0]] 

def allFours(board):
    for i in rows(board):
        yield i
    for i in columns(board):
        yield i
    for i in diagonals(board):
        yield i

def hasDots(board):
    return '.' in board[0] or '.' in board[1] or '.' in board[2] or '.' in board[3]

def gameResult(board):
    completed = not hasDots(board)
    for i in allFours(board):
        w = winner(i)
        if w:
            return w + " won"
    return "Draw" if completed else "Game has not completed"

if __name__ == "__main__":
    cases = int(sys.stdin.readline())
    for i in xrange(cases):
        board = []
        for j in xrange(4):
            board.append(sys.stdin.readline().strip())
        sys.stdin.readline() # skip empty line
        result = gameResult(board)
        print("Case #{}: {}".format(i + 1, result))
