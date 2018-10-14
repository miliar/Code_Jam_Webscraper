#!/usr/bin/env python3

import sys

def nextline():
    return sys.stdin.readline()

def read_line(line):
    rows = []
    for i in range(4):
        p = map(int, nextline().split())
        rows.append(p)
    return set(rows[line-1])

def go(tc):
    n1 = int(nextline())
    line1 = read_line(n1)
    n2 = int(nextline())
    line2 = read_line(n2)

    diff = line2 & line1
    if len(diff) == 1:
        print("Case #{}: {}".format(tc, diff.pop()))
    elif len(diff) == 0:
        print("Case #{}: Volunteer cheated!".format(tc))
    else:
        print("Case #{}: Bad magician!".format(tc))

TC = int(nextline())
for tc in range(1, TC+1):
    go(tc)

