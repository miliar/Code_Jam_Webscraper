#!/usr/bin/env python
import sys
import IPython

def get_rows(lines):
    return lines[:]

def get_cols(lines):

    cols = [''] * 4
    s = ''.join(lines)

    for x in xrange(4):
        cols[x] = s[x::4]

    return cols

def get_diags(lines):
    s = ''.join(lines)
    d1 = ''
    for x in xrange(4):
        d1 += s[x+4*x]

    d2 = ''
    for x in xrange(4):
        d2 += s[4*(x+1)-(x+1)]

    return d1, d2

def handle_game(lines):
    outs = {'X' : 'X won',
            'O' : 'O won',
            'D' : 'Draw',
            'N' : 'Game has not completed'
           }

    rows = get_rows(lines)
    for row in rows:
        if row.count('X') == 4:
            return outs['X']
        elif row.count('X') == 3 and row.count('T') == 1:
            return outs['X']

        if row.count('O') == 4:
            return outs['O']
        elif row.count('O') == 3 and row.count('T') == 1:
            return outs['O']


    cols = get_cols(lines)
    for col in cols:
        if col.count('X') == 4:
            return outs['X']
        elif col.count('X') == 3 and col.count('T') == 1:
            return outs['X']

        if col.count('O') == 4:
            return outs['O']
        elif col.count('O') == 3 and col.count('T') == 1:
            return outs['O']

    diags = get_diags(lines)
    for diag in diags:
        if diag.count('X') == 4:
            return outs['X']
        elif diag.count('X') == 3 and diag.count('T') == 1:
            return outs['X']

        if diag.count('O') == 4:
            return outs['O']
        elif diag.count('O') == 3 and diag.count('T') == 1:
            return outs['O']

    for line in lines:
        if line.count('.') > 0:
            return outs['N']

    return outs['D']


lines = open(sys.argv[1]).read().split('\n')

num = int(lines[0])

idx = 1
for test_idx, x in enumerate(xrange(num)):
    out = handle_game(lines[idx:idx+4])
    idx += 5
    print 'Case #%s: %s' % (test_idx+1, out)
