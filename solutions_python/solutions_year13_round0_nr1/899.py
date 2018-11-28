#!/usr/bin/env python2

import sys

def boards(filename):
    with open(filename) as f:
        ncases = int(f.readline())
        boards = [board.split('\n') for board in f.read().strip().split('\n\n')]
    return boards

def won(board, player):
    rows = [row.replace('T', player) for row in board]
    cols = [''.join([rows[i][j] for i in range(4)]) for j in range(4)]
    diag1 = ''.join([rows[i][i] for i in range(4)])
    diag2 = ''.join([rows[i][3-i] for i in range(4)])
    return 4 * player in (rows + cols + [diag1, diag2])

filename = sys.argv[1]
for case, board in enumerate(boards(filename), 1):
    won1, won2 = won(board, 'X'), won(board, 'O')
    complete = all('.' not in row for row in board)
    if (won1 and won2) or (complete and not won1 and not won2):
        print 'Case #{0}: Draw'.format(case)
    elif won1:
        print 'Case #{0}: X won'.format(case)
    elif won2:
        print 'Case #{0}: O won'.format(case)
    else:
        print 'Case #{0}: Game has not completed'.format(case)

