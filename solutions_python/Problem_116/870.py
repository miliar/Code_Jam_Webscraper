#!/usr/bin/python3

import sys

def check(field, sx, sy, dx, dy):
    resx = 0
    reso = 0
    for i in range(0,4):
        c = field[sx + i*dx][sy + i*dy]
        if c == 'X': resx += 1
        elif c == 'O': reso += 1
        elif c == 'T':
            resx += 1
            reso += 1
    if resx == 4: return 1, "X won"
    if reso == 4: return 2, "O won"
    return 0, ""

def case():
    field = list()
    for i in range(0,4):
        field.append(sys.stdin.readline().strip())
    sys.stdin.readline()
    for i in range(0,4):
        r, msg = check(field, 0, i, 1, 0)
        if r: return msg
        r, msg = check(field, i, 0, 0, 1)
        if r: return msg
    r, msg = check(field, 0, 0, 1,1)
    if r: return msg
    r, msg = check(field, 0, 3, 1,-1)
    if r: return msg
    for i in range(0,4):
        for j in range(0,4):
            if field[i][j] == '.': return "Game has not completed"
    return "Draw"

T = int(sys.stdin.readline())
for i in range(1,T+1):
    print("Case #%s: %s" % (i, case()))
    

