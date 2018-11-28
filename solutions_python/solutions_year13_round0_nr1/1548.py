# encoding: utf-8
import sys

def who_won(b):
    # row
    for r in xrange(0, 4):
        player = b[r][0]
        if player == '.':
            # skip this row
            continue
        won = True
        for c in xrange(1, 4):
            if b[r][c] != player and b[r][c] != 'T':
                won = False
                break;
        if won:
            return '%s won' % player
    
    # column
    for c in xrange(0, 4):
        player = b[0][c]
        if player == '.':
            # skip this column
            continue
        won = True
        for r in xrange(1, 4):
            if b[r][c] != player  and b[r][c] != 'T':
                won = False
                break;
        if won:
            return '%s won' % player
    
    # counter diagonal
    player = b[0][0]
    won = True
    if player != '.':
        for i in xrange(1, 4):
            if b[i][i] != player and b[i][i] != 'T':
                won = False
                break;
        if won:
            return '%s won' % player
    # diagonal
    player = b[0][3]
    won= True
    if player != '.':
        for i in xrange(1, 4):
            if b[i][3-i] != player  and b[i][3-i] != 'T':
                won = False
                break;
        if won:
            return '%s won' % player
    
    # nobody won, Draw or Game has not compeleted
    draw   = True
    for r in xrange(0, 4):
        for c in xrange(0, 4):
            if b[r][c] == '.':
                draw = False
    
    if draw:
        return 'Draw'
    else:
        return 'Game has not completed'

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for t in xrange(1, T+1):
        board = []
        for r in xrange(0, 4):
            board.append(sys.stdin.readline().rstrip())
        sys.stdin.readline()
        status = who_won(board)
        print 'Case #%d: %s' % (t, status)