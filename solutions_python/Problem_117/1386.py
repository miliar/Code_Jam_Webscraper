def check(board):
    h = [max(row) for row in board]
    v = [max(row[i] for row in board) for i in range(m)]
    for i in range(n):
        for j in range(m):
            if board[i][j] != v[j] and  board[i][j] != h[i]:
                return False
    return True

for t in range(input()):
    print "Case #%s:" % str(t + 1),
    n, m = map(int, raw_input().split())
    board = [map(int, raw_input().split()) for i in range(n)]
    if check(board):
        print "YES"
    else:
        print "NO"

