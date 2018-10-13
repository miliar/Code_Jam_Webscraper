import sys

def score(brd):
    for i in xrange(4):
        if brd[i][i] == '.': continue
        if all(brd[i][0] == brd[i][j] for j in xrange(1, 4)):
            return brd[i][0]
        if all(brd[0][i] == brd[j][i] for j in xrange(1, 4)):
            return brd[i][0]
    
    if all(brd[i][i] == brd[i+1][i+1] for i in xrange(0, 3)):
        if brd[0][0] != '.':
            return brd[0][0]
    if all(brd[3-i][i] == brd[2-i][i+1] for i in xrange(0, 3)):
        if brd[3][0] != '.':
            return brd[3][0]
    return None

def draw(board):
    return not any('.' in row for row in board)

#Read the board now. The board is a 3x3 array filled with X, O or _.
k = int(raw_input())

for j in xrange(1, k+1):
    if j != 1:
        raw_input()
    
    board = []
    x_board = []
    o_board = []
    
    for i in xrange(0, 4):
        board.append([c for c in raw_input()])
        x_board.append(['X' if c == 'T' else c for c in board[-1]])
        o_board.append(['O' if c == 'T' else c for c in board[-1]])
    
    sys.stdout.write('Case #%d: ' % j)

    res = None
    for i in [x_board, o_board]:
        res = score(i)
        if res:
            print "%s won" % res
            break
    if res: continue
    
    if draw(board):
        print "Draw"
        continue
    print "Game has not completed"
