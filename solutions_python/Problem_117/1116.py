nrows, ncols = 3, 3

def check_row(val, r):
    for i in range(ncols):
        if board[r][i] > val:
            return False
    return True

def check_col(val, c):
    for i in range(nrows):
        if board[i][c] > val:
            return False
    return True

def check_cell(r, c):
    val = board[r][c]
    return check_row(val, r) or check_col(val, c)

def check_board():
    for i in range(nrows):
        for j in range(ncols):
            if not check_cell(i, j):
                return False
    return True

ts = int(raw_input())
for t in range(ts):
    nrows, ncols = map(int, raw_input().split(' '))
    board = {}
    for row in range(nrows):
        board[row] = map(int, raw_input().split(' '))
    print "Case #%d: %s" % (t+1, "YES" if check_board() else "NO")
