#!/usr/bin/python

import sys

T = int(sys.stdin.readline().strip())
for ncase in range(T):
    a1 = int(sys.stdin.readline().strip())
    grid1 = []
    for i in range(4):
        grid1.append(sys.stdin.readline().strip().split(' '))
    answ1 = set(grid1[a1-1])
    a2 = int(sys.stdin.readline().strip())
    grid2 = []
    for i in range(4):
        grid2.append(sys.stdin.readline().strip().split(' '))
    answ2 = set(grid2[a2-1])
    answ = answ1.intersection(answ2)
    if len(answ) == 0:
        s = "Volunteer cheated!"
    if len(answ) > 1:
        s = "Bad magician!"
    if len(answ) == 1:
        s = str((list(answ))[0])
    print ("Case #%d: %s" % (ncase+1, s))



