#!/usr/bin/env python

import sys

file = open(sys.argv[1], "r")
cases = int(file.readline())

for n in xrange(1, cases + 1):
    game = map(int, file.readline().split())
    omino = game[0]
    size = game[1:]
    if omino == 1:
        winner = "GABRIEL"
    elif omino == 2:
        if (size[0]*size[1])%2 == 0:
            winner = "GABRIEL"
        else:
            winner = "RICHARD"
    elif omino == 3:
        size = sorted(size)
        winner = "RICHARD"
        if size[0] == 2 and size[1] == 3:
            winner = "GABRIEL"
        elif size[0] == 3 and size[1] == 3:
            winner = "GABRIEL"
        elif size[0] == 3 and size[1] == 4:
            winner = "GABRIEL"
    elif omino == 4:
        size = sorted(size)
        winner = "RICHARD"
        if size[0] == 3 and size[1] == 4:
            winner = "GABRIEL"
        if size[0] == 4 and size[1] == 4:
            winner = "GABRIEL"
    
    print "Case #{}: {}".format(n, winner)
