#! /opt/local/bin/python

import sys, itertools

def getline(file=sys.stdin):
    return file.readline().strip()

def getcells():
    return list(getline())

def out(s):
    if False:
        print s

def cols(rows):
    return [[row[c] for row in rows] for c in range(4)]

def diags(rows):
    return [[rows[0][0], rows[1][1], rows[2][2], rows[3][3]],
            [rows[0][3], rows[1][2], rows[2][1], rows[3][0]]]

def winner(cells):
    xs = os = ts = 0
    for cell in cells:
        if cell == 'X':
            xs += 1
        elif cell == 'O':
            os += 1
        elif cell == 'T':
            ts += 1
    if xs + ts == 4:
        return 'X'
    elif os + ts == 4:
        return 'O'
    else:
        return None

def solve(casenum):
    rows = []
    full = True
    for r in range(4):
        rows.append(getcells())
        if '.' in rows[-1]:
            full = False
    getline()                           # blank line for some reason

    results = {'X': 0, 'O': 0, None: 0}
    for x in rows + cols(rows) + diags(rows):
        results[winner(x)] += 1

    if results['X'] > results['O']:
        answer = 'X won'
    elif results['O'] > results['X']:
        answer = 'O won'
    elif full:
        answer = 'Draw'
    else:
        answer = 'Game has not completed'

    print 'Case #%d: %s' % (casenum, answer)

cases = int(getline())
for case in xrange(cases):
    solve(case + 1)
