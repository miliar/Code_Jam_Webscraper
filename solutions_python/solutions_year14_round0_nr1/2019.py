#!/usr/bin/env python3

import sys

T = int(next(sys.stdin))

for x in range(1, T+1):
    q1 = int(next(sys.stdin).strip())
    layout1 = [[int(dig) for dig in row.split()] for row in [next(sys.stdin) for _ in range(4)]]
    q2 = int(next(sys.stdin).strip())
    layout2 = [[int(dig) for dig in row.split()] for row in [next(sys.stdin) for _ in range(4)]]

    possibles = layout1[q1-1]
    goodcount = 0
    for p2 in layout2[q2-1]:
        if p2 in possibles:
            y = p2
            goodcount += 1
    if not goodcount:
        y = "Volunteer cheated!"
    elif goodcount>1:
        y = "Bad magician!"


    print("Case #{}: {}".format(x, y))
