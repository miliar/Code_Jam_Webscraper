#!/usr/bin/env python

import sys
import numpy as np

infile = open(sys.argv[1], 'rb')

lines = infile.readlines()

n_cases = int(lines.pop(0))

statuses = ['X won', 'O won', 'Draw',
            'Game has not completed']
t_score = 50
x_score = 1
o_score = 10

x_win_scores = set([4*x_score, 3*x_score + t_score])
o_win_scores = set([4*o_score, 3*o_score + t_score])
draw_scores = set([3*x_score + o_score, 2*x_score + 2*o_score,
                  x_score + 3*o_score,
                  2*x_score + o_score + t_score,
                  x_score + 2*o_score + t_score])

for icase in range(1, n_cases+1):
    # read board
    board = np.zeros([4,4], dtype=int)
    t_pos = None
    for irow in range(4):
        row = lines.pop(0)
        for icol, char in enumerate(row):
            if char == 'X':
                board[irow,icol] = x_score
            elif char == 'O':
                board[irow,icol] = o_score
            elif char == 'T':
                board[irow,icol] = t_score
            else:
                pass

    # get sums
    col_sums = set(np.sum(board, axis=0))
    row_sums = set(np.sum(board, axis=1))
    diag_sums = set([np.trace(board), np.trace(np.rot90(board))])
    all_sums = col_sums | row_sums | diag_sums
    
    # check scores
    if len(all_sums & x_win_scores) > 0:
        status = 0
    elif len(all_sums & o_win_scores) > 0:
        status = 1
    elif len(all_sums & draw_scores) > 0:
        status = 2
    else:
        status = 3

    print "Case #%d: %s" % (icase, statuses[status])

    # discard blank row
    if len(lines) > 0:
        discard = lines.pop(0)
