#!/usr/bin/env python

def solve(A, sizes, changes=None):
    if changes is None:
        sizes = sorted(sizes)
        changes = 0
    if A == 1:
        return changes + len(sizes)
    while sizes and sizes[0] < A:
        A += sizes.pop(0)
    if not sizes:
        return changes
    changes += 1
    return min(solve(A, sizes[1:], changes), solve(2*A - 1, list(sizes), changes))

T = int(raw_input())
for t in range(T):
    A, N = [int(j) for j in raw_input().split()]
    sizes = [int(j) for j in raw_input().split()]
    print "Case #%d: %d" % (t+1, solve(A, sizes))
