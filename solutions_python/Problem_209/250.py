
from math import pi

from sys import setrecursionlimit
setrecursionlimit(10000)

NINF = -10**18


def solve(t):
    N, K = map(int, raw_input().split())

    pancakes = []

    for _ in xrange(N):
        r, h = map(int, raw_input().split())
        pancakes.append((r, h))
    pancakes.sort()
    pancakes = pancakes[::-1]

    memo = {}

    def find(ix, rem):
        if rem == 0:
            return 0.0
        if ix + rem > N:
            return NINF
        if (ix, rem) in memo:
            return memo[(ix, rem)]

        ans = find(ix+1, rem)

        tmp = 0.0
        r, h = pancakes[ix]
        if rem == K:
            tmp += pi * r * r
        tmp += 2 * pi * r * h
        tmp += find(ix+1, rem-1)

        ans = max(ans, tmp)

        memo[(ix, rem)] = ans
        return ans

    ans = find(0, K)

    print 'Case #%d: %.12f' % (t, ans)

T = input()
for i in xrange(T):
    solve(i+1)
