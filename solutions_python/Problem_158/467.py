#!/usr/bin/python3

import sys

ncases = int(sys.stdin.readline().strip())

for t in range(1, ncases+1):
    values = sys.stdin.readline().split()
    x = int(values[0])
    r = int(values[1])
    c = int(values[2])

    # Really nasty "algorithm", I don't feel proud of this :D

    if (r * c) % x != 0:
        winner = "RICHARD" # Quick exit: number of squares is not multiple of X
    elif x == 1:
        winner = "GABRIEL" # Impossible for Richard with 1-square shapes
    elif x == 2:
        winner = "GABRIEL" # Unless odd number of squares, covered above
    elif x == 3:
        if r==1 or c==1:
            winner = "RICHARD" # Only chance, row-style square where the L shape doesn't fit
        else:
            winner = "GABRIEL"
    elif x == 4:
        if r<3 or c<3:
            winner = "RICHARD" # Impossible for Gabriel on 1 or 2-row squares
        else:
            winner = "GABRIEL"


    print("Case #{0}: {1}".format(t, winner))

