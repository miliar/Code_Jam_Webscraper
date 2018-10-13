#!/usr/bin/python

from sys import stdin

def solve(A, motes):
    if (A == 1):
        return len(motes)
    op = 0
    min_remove_op = float("inf")
    armin = A
    queue = sorted(motes)
    for i, mote in enumerate(queue):
        min_remove_op = min(len(queue) - i + op, min_remove_op)
        while armin <= mote:
            armin += armin - 1
            op += 1
            if op >= min_remove_op:
                return min_remove_op
        armin += mote
    return min(op, min_remove_op)

T = int(stdin.readline())
for i in range(T):
    A, N = map(int, stdin.readline().split())
    motes = map(int, stdin.readline().split())
    print "Case #%d: %d" % (i + 1, solve(A, motes))
