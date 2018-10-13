#!/usr/bin/python

import sys


def solve(perm):
    n = len(perm)
    ans = 0
    seen = [False] * n
    for i in range(n):
        if seen[i]:
            continue
        seen[i] = True
        pos = i
        cyclen = 1
        while perm[pos] != i:
            pos = perm[pos]
            seen[pos] = True
            cyclen += 1
        if cyclen > 1:
            ans += cyclen
    return ans


if __name__ == "__main__":
    tests = int(sys.stdin.readline())
    for t in range(tests):
        n = int(sys.stdin.readline())
        perm = map(int, sys.stdin.readline().split())
        perm = map(lambda x: x-1, perm)
        assert len(perm) == n
        ans = solve(perm)
        print "Case #%d: %f" % (t + 1, ans)
