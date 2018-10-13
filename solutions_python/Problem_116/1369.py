import sys
import re

getl = lambda : sys.stdin.readline().strip()

xmatches = ['XXXX']
xt = 'TXXX'
for i in range(4):
    xmatches.append(xt[i:] + xt[:i])
omatches = ['OOOO']
ot = 'TOOO'
for i in range(4):
    omatches.append(ot[i:] + ot[:i])

cases = range(int(getl()))
for case in cases:
    board = []
    for i in range(4):
        board.append(getl())
    getl()
    h = len(board)
    w = len(board[0])
    result = None
    hasdots = False

    for i in range(4):
        if '.' in board[i]:
            hasdots = True
        if board[i] in xmatches:
            result = 'X won'
        elif board[i] in omatches:
            result = 'O won'

    if result is None:
        board = list(zip(*board))
        board = list(map(lambda x: ''.join(x), board))
        for i in range(4):
            if board[i] in xmatches:
                result = 'X won'
            elif board[i] in omatches:
                result = 'O won'

    if result is None:
        s = ''
        t = ''
        for i in range(4):
            s += board[i][i]
            t += board[i][3-i]

        if s in xmatches or t in xmatches:
            result = 'X won'
        elif s in omatches or t in omatches:
            result = 'O won'

    if result is None:
        if hasdots:
            result = 'Game has not completed'
        else:
            result = 'Draw'

    print('Case #{0}: {1}'.format(case+1, result))
