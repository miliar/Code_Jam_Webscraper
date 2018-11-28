import sys, math, re, itertools as it, bisect, string
from collections import (defaultdict, deque)

arrow = "^<>v"
dxy = {"^":[0, -1], "v":[0, 1], "<":[-1, 0], ">":[1, 0]}

def check(c, r, dx, dy):
    c += dx; r += dy
    while 0 <= c < C and 0 <= r < R:
        if A[r][c] in arrow:
            return True
        c += dx; r += dy
    return False

T = int(raw_input())
for case in xrange(1, T + 1):
    R, C = map(int, raw_input().split())
    A = [list(raw_input()) for i in xrange(R)]

    ans = 0
    for r in xrange(R):
        for c in xrange(C):
            if A[r][c] in arrow:
                dx, dy = dxy[A[r][c]]
                if check(c, r, dx, dy):
                    continue
                else:
                    for dx, dy in zip([1, 0, -1, 0],[0, 1, 0, -1]):
                        if check(c, r, dx, dy):
                            ans += 1
                            break
                    else:
                        ans = "IMPOSSIBLE"
                        break

        if ans == "IMPOSSIBLE":
            break
    print "Case #%d: %s" % (case, ans)
