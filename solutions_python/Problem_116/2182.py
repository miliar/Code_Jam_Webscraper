import sys


f = sys.stdin
for PROB in xrange(int(f.readline())):
    board=[f.readline().strip(),f.readline().strip(),f.readline().strip(),f.readline().strip()]
    f.readline()
    won = False
    xx,yy,XX,YY = 0,0,0,0
    for i in range(4):
        X,Y,x,y=0,0,0,0
        for j in range(4):
            if board[i][j] in ['X','T']: X = X + 1
            if board[i][j] in ['O','T']: Y = Y + 1
            if board[j][i] in ['X','T']: x = x + 1
            if board[j][i] in ['O','T']: y = y + 1
        if X==4 or x==4: won = 'X'
        if Y==4 or y==4: won = 'O'
        if won: break
        if board[i][i] in ['X','T']: xx = xx + 1
        if board[i][i] in ['O','T']: yy = yy + 1
        if board[3-i][i] in ['X','T']: XX = XX + 1
        if board[3-i][i] in ['O','T']: YY = YY + 1

    if xx==4 or XX==4: won = 'X'
    if yy==4 or YY==4: won = 'O'
    if won: print 'Case #%s: %s won'%(PROB+1,won)
    elif sum([1 for i in board if '.' in i])>0: print 'Case #%s: Game has not completed'%(PROB+1)
    else:  print 'Case #%s: Draw'%(PROB+1)

