#!/usr/bin/python

import sys

def emit(text, *args):
    msg = text % args
    sys.stderr.write(msg)
    sys.stdout.write(msg)

def getline():
    return sys.stdin.readline().rstrip('\n')

scans = (
    (0, 0, 1, 0),
    (0, 1, 1, 0),
    (0, 2, 1, 0),
    (0, 3, 1, 0),
    (0, 0, 0, 1),
    (1, 0, 0, 1),
    (2, 0, 0, 1),
    (3, 0, 0, 1),
    (0, 0, 1, 1),
    (0, 3, 1, -1)
)

def solve(lines):
    maybe_draw = True
    for x, y, dx, dy in scans:
        maybe_X = True
        maybe_O = True
        for i in range(4):
            c = lines[y + i * dy][x + i * dx]
            if c == 'X' or c == '.':
                maybe_O = False
            if c == 'O' or c == '.':
                maybe_X = False
            if c == '.':
                maybe_draw = False
        if maybe_X:
            return "X won"
        if maybe_O:
            return "O won"
    if maybe_draw:
        return "Draw"
    return "Game has not completed"

ncases = int(getline())

for casenr in range(1, ncases+1):
    lines = [ getline() for x in range(4) ]
    getline() # skip empty line
    emit("Case #%d: %s\n", casenr, solve(lines))
