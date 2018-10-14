#!/usr/bin/python
import sys, math        

T = int(sys.stdin.readline())
for t in range(T):
    x, r, c = map(int, sys.stdin.readline().strip().split(" "))
    selector = "RICHARD"
    player =  "GABRIEL"
    if x == 1:
        winner = player
    elif x == 2:
        if (r * c) % 2 == 0:
            winner = player
        else:
            winner = selector
    elif x == 3:
        if (r * c) % 3 != 0 or r == 1 or c == 1:
            winner = selector
        else:
            winner = player
    elif x == 4:
        if (r * c) % 4 != 0 or r <= 2 or c <= 2:
            winner = selector
        else:
            winner = player
        
    print "Case #%d: %s" % ((t + 1), winner)
