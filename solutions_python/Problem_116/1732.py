#!/usr/bin/env python

def check_line(q):
    i = 0
    # if there is a . in any position, the game is not over
    if (q.count('X') == 3 and q.count('T') == 1) or q.count('X') == 4:
        return (True, 'X won')
    if (q.count('O') == 3 and q.count('T') == 1) or q.count('O') == 4:
        return (True, 'O won')
    else:
        return (False, None)

def test_case(c, i):
    prefix =  'Case #%d:' % (i+1)
    dots = False
    # check rows
    for row in c:
        res = check_line(row)
        if res[0]:
           print prefix, res[1]
           return
    # check cols
    for col_idx in xrange(4):
        col = [row[col_idx] for row in c]
        res = check_line(col)
        if res[0]:
            print prefix, res[1]
            return
    # check main diag
    res = check_line([c[i][i] for i in xrange(4)])
    if res[0]:
        print prefix, res[1]
        return
    # check other diag
    res = check_line([c[i][3 - i] for i in xrange(4)])
    if res[0]:
        print prefix, res[1]
        return
    # check for dots
    for line in c:
        if '.' in line:
            print prefix, 'Game has not completed'
            return
    print prefix, 'Draw'

with open('input.in') as f:
    n = int(f.readline())
    for i in range(0, n):
        case = [f.readline().strip() for x in xrange(4)]
        test_case(case, i)
        f.readline()
