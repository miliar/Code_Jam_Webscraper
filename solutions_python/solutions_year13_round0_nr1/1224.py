N = 4

def check(row):
    row = set(row)
    if '.' in row:
        return True
    if len(row) == 1:
        raise Exception(iter(row).next() + " won")
    if len(row) == 2 and 'T' in row:
        raise Exception(iter(row-set('T')).next() + " won")
    return False

def transp(board):
    new = [['.' for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            new[j][i] = board[i][j]
    return new

def diags(board):
    d1 = []
    d2 = []
    for i in range(N):
        d1.append(board[i][i])
        d2.append(board[i][N-i-1])
    return d1, d2

def f(board):
    dot = False
    for row in board:
        dot = check(row) or dot
    for col in transp(board):
        dot = check(col) or dot
    for d in diags(board):
        check(d)
    if dot:
        raise Exception("Game has not completed")
    raise Exception("Draw")

if __name__ == "__main__":
    T = int(raw_input())
    case = 1
    for i in range(T):
        board = []
        for j in range(N):
            board.append(raw_input())
        try:
            f(board)
            print "what"
            exit()
        except Exception, e:
            print "Case #{}: {}".format(case, e.message)
        case += 1
        raw_input() # newline
