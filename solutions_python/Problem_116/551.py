#!/usr/bin/python
import sys

# Tic-Tac-Toe-Tomek

lines = [l.rstrip() for l in sys.stdin.readlines()]
for x in xrange(int(lines.pop(0))):
    result = "Draw"
    rows = lines[5*x:5*x+4]
    cols = [''.join([rows[r][c] for r in xrange(4)]) for c in xrange(4)]
    diag = [''.join([rows[d][d] for d in xrange(4)]), ''.join([rows[d][3-d] for d in xrange(4)])]
    for r in [row for lists in [rows, cols, diag] for row in lists]:
        for c in ['X', 'O']:
            if r.count(c) == 4 - r.count('T'):
                result = c + " won"
    if result == "Draw" and ''.join(rows).count('.') > 0:
        result = "Game has not completed"
    print("Case #%u: %s" % (x + 1, result))
