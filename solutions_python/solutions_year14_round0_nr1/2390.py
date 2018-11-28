#!/usr/bin/python
import sys

T = int(sys.stdin.readline())
for i in xrange(T):
    print "Case #%d:" % (i+1),
    valid = set()
    l1 = int(sys.stdin.readline())
    board = []
    for j in xrange(4):
        row = map(int, sys.stdin.readline().split(" "))
        board.append(row)
    valid = set(board[l1-1])
    l2 = int(sys.stdin.readline())
    board = []
    for j in xrange(4):
        row = map(int, sys.stdin.readline().split(" "))
        board.append(row)
    valid = valid.intersection(set(board[l2-1]))
    if len(valid) == 0:
        print "Volunteer cheated!"
    elif len(valid) > 1:
        print "Bad magician!"
    else:
        print valid.pop()
