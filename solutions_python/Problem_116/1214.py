import sys

def testcase(board):
    rows = [ (0,0), (0,0), (0,0), (0,0) ]
    cols = [ (0,0), (0,0), (0,0), (0,0) ]
    diag = (0,0)
    antidiag = (0,0)
    empty = False
    for i in xrange(4):
        for j in xrange(4):
            if board[i][j] == 'X':
                add = (1,0)
            elif board[i][j] == 'O':
                add = (0, 1)
            elif board[i][j] == 'T':
                add = (1,1)
            else:
                add = (0,0)
                empty = True
            rows[i] = (rows[i][0] + add[0], rows[i][1] + add[1])
            cols[j] = (cols[j][0] + add[0], cols[j][1] + add[1])
            if i == j:
                diag = (diag[0] + add[0], diag[1] + add[1])
            elif i + j == 3:
                antidiag = (antidiag[0] + add[0], antidiag[1] + add[1])
    for x,o in rows + cols + [diag, antidiag]:
        if x == 4:
            return "X won"
        elif o == 4:
            return "O won"
    if empty:
        return "Game has not completed"
    else:
        return "Draw"
i = 1
board = []
first = True
for line in sys.stdin:
    if len(line) != 5 or first:
        first = False
        continue
    board.append(line[:-1])
    if len(board) == 4:
        print "Case #%d: %s" % (i, testcase(board))
        board = []
        i += 1
