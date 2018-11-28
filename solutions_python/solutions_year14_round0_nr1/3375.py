#!/usr/bin/env python
import sys

line = sys.stdin.readline().strip()
cases = int(line)

for i in range(cases):
    row1 = int(sys.stdin.readline().strip())
    board = []
    can1 = []
    for j in range(4):
        board.append( map(int, sys.stdin.readline().strip().split(' ')))
        if j+1 == row1:
            can1 = board[j]
    row2 = int(sys.stdin.readline().strip())
    board = []
    can2 = []
    for j in range(4):
        board.append( map(int, sys.stdin.readline().strip().split(' ')))
        if j+1 == row2:
            can2 = board[j]
    ans = []
    for j in can1:
        for k in can2:
            if j == k:
                ans.append(j)
    sys.stdout.write("Case #%d: " % (i+1))
    if len(ans) >= 2:
        sys.stdout.write("Bad magician!\n")
    elif len(ans) == 0:
        sys.stdout.write("Volunteer cheated!\n")
    else:
        sys.stdout.write("%d\n" % ans[0])



