#!/usr/bin/env python


def check(board):
    # Horizontal
    for i in xrange(4):
        if board[i][0] == '.':
            continue
        l = [board[i][0]]
        for j in xrange(1, 4):
            value = board[i][j]
            if value != l[-1] and value != 'T':
                break
            l.append(value)
        if len(l) == 4:
            return "%s won" % l[0]

    # Vertical
    for i in xrange(4):
        if board[0][i] == '.':
            continue
        l = [board[0][i]]
        for j in xrange(1, 4):
            value = board[j][i]
            if value != l[-1] and value != 'T':
                break
            l.append(value)
        if len(l) == 4:
            return "%s won" % l[0]

    # Diagonal l->r
    if board[0][0] != '.':
        l = [board[0][0]]
        for i in xrange(1, 4):
            value = board[i][i]
            if value != l[-1] and value != 'T':
                break
            l.append(value)
        if len(l) == 4:
            return "%s won" % l[0]

    # Diagonal l->r
    if board[0][3] != '.':
        l = [board[0][3]]
        for i in xrange(1, 4):
            value = board[i][3-i]
            if value != l[-1] and value != 'T':
                break
            l.append(value)
        if len(l) == 4:
            return "%s won" % l[0]

    for line in board:
        for char in line:
            if char == '.':
                return 'Game has not completed'

    return 'Draw'

import sys
data = open(sys.argv[1], 'r').read()
data = data.split('\n')
data.reverse()
T = int(data[-1])
for i in xrange(T):
    data.pop()
    board = []
    for line in xrange(4):
        board.append(list(data.pop()))
    print 'Case #%s: %s' % (i + 1, check(board))
