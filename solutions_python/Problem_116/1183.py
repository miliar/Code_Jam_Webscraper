# Python 2.7.2

import sys

stdin = sys.stdin.readlines()
cases = int(stdin.pop(0))
for i in xrange(cases):
    board = []
    incomplete = False
    owin = False
    xwin = False
    for j in stdin[i*5:(i+1)*5]:
        if j.strip() != '':
            board.append(list(j))
    rowcolcount = []
    diag = [[0, 0,], [0, 0]]
    for j in xrange(4):
        rowcolcount.append([0, 0, 0, 0])
    for j in xrange(4):
        for k in xrange(4):
            if board[j][k] == 'T':
                rowcolcount[0][j] += 1
                rowcolcount[1][j] += 1
                rowcolcount[2][k] += 1
                rowcolcount[3][k] += 1
                if j == k:
                    diag[0][0] += 1
                    diag[1][0] += 1
                if j+k == 3:
                    diag[0][1] += 1
                    diag[1][1] += 1
            elif board[j][k] == 'X':
                rowcolcount[1][j] += 1
                rowcolcount[3][k] += 1
                if j == k:
                    diag[0][0] += 1
                if j+k == 3:
                    diag[0][1] += 1
            elif board[j][k] == 'O':
                rowcolcount[0][j] += 1
                rowcolcount[2][k] += 1
                if j == k:
                    diag[1][0] += 1
                if j+k == 3:
                    diag[1][1] += 1
            elif not incomplete:
                incomplete = True
    for j in xrange(4):
        for k in xrange(4):
            if xwin or owin:
                break
            if rowcolcount[j][k] == 4:
                if j%2 == 0:
                    owin = True
                else:
                    xwin = True
        if xwin or owin:
            break
    if (not owin) and (not xwin):
        for j in xrange(2):
            if diag[0][j] == 4:
                xwin = True
            if diag[1][j] == 4:
                owin = True
    if owin:
        print "Case #"+str(i+1)+": O won"
    elif xwin:
        print "Case #"+str(i+1)+": X won"
    elif incomplete:
        print "Case #"+str(i+1)+": Game has not completed"
    else:
        print "Case #"+str(i+1)+": Draw"
                
