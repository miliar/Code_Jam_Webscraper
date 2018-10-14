# -*- coding: utf-8 -*-

import sys
fin = sys.stdin
T = int(fin.readline())


def calc(v, c):
    for ch in v:
        yield 1 if ch == c else 0

d = 0

def check(v):
    global d
    d += sum(calc(v, '.'))
    t = sum(calc(v, 'T'))

    x = sum(calc(v, 'X'))
    o = sum(calc(v, 'O'))

    if x == 4 or x == 3 and t == 1:
        return "X won"

    if o == 4 or o == 3 and t == 1:
        return "O won"

def solve(b):
    for i in xrange(4):
        w = check((b[i][0], b[i][1], b[i][2], b[i][3]))
        if w:
            return w

        w = check((b[0][i], b[1][i], b[2][i], b[3][i]))
        if w:
            return w

    w = check((b[0][0], b[1][1], b[2][2], b[3][3]))
    if w:
        return w

    w = check((b[0][3], b[1][2], b[2][1], b[3][0]))
    if w:
        return w

    return "Draw" if d == 0 else "Game has not completed"

for case in xrange(1,T+1):
    b = []
    d = 0
    for i in xrange(4):
        r = fin.readline()
        b.append(r[:])

    fin.readline()
    
    print "Case #%d: %s" % (case, solve(b))