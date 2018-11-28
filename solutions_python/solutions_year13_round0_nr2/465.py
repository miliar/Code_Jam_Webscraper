import sys


def calc(board):
    x = []
    y = []
    for i in range(len(board)):
        m = -1
        for j in range(len(board[i])):
            if board[i][j] > m:
                m = board[i][j]
        x.append(m)
    
    for j in range(len(board[0])):
        m = -1
        for i in range(len(board)):
            if board[i][j] > m:
                m = board[i][j]
        y.append(m)
    
    possible = True
    for i in range(len(board)):
        for j in range(len(board[i])):
            possible = possible and ((board[i][j] == x[i]) or (board[i][j] == y[j]))
            if not possible:
                return False            
    return possible

t = int(sys.stdin.readline())
for i in range(t):
    (n, m) = map(int, sys.stdin.readline().split())
    board = []
    for j in range(n):
        board.append(list(map(int, sys.stdin.readline().split())))
    res = ""
    if calc(board):
        res = "YES";
    else:
        res = "NO";
    
    print("Case #%d: %s" % (i + 1, res))