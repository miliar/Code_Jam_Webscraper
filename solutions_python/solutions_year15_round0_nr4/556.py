#!/usr/bin/python

import sys

def emit(text, *args):
    msg = text % args
    sys.stderr.write(msg)
    sys.stdout.write(msg)

def getline():
    return sys.stdin.readline().rstrip('\n')

def solve(x, r, c):
    if (r * c) % x != 0:
        return "RICHARD"  # R * C can't be filled with X-ominoes
    if x >= 7:
        return "RICHARD"  # Richard can pick an X-omino with an internal hole
    # how large can Richard force the X-omino to be?
    awkward = (x - 1) // 2 + 1
    if awkward > r or awkward > c:
        return "RICHARD"  # Richard can pick an X-omino that will not fit
    if x > 3 and awkward == min(r, c):
        return "RICHARD"  # Richard can pick an X-omino that leaves uneven size
    if x - min(r, c) >= max(r, c):
        return "RICHARD"  # Richard can pick an X-omino that will not fit
    return "GABRIEL"

ncases = int(getline())

for casenr in range(1, ncases+1):
    x, r, c = [ int(s) for s in getline().split() ]
    emit("Case #%d: %s\n", casenr, solve(x, r, c))
