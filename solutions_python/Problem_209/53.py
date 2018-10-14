import math
import fractions

def solve(pancs, N, K):
    cache = [[None] * N]

    for i in xrange(N):
        cache.append([None] * N)

    for i in xrange(N):
        cache[0][i] = 0

    for k in xrange(1, N + 1):
        for n in xrange(N):
            R, H = pancs[n]
            added = 2*R*H
            if k == 1:
                # if we take, we know the radii
                added += R*R

            pos = [cache[k - 1][i] for i in xrange(n) if cache[k-1][i] is not None]
            if len(pos) == 0:
                cache[k][n] = added
            else:
                cache[k][n] = max([cache[k - 1][i] for i in xrange(n)]) + added

    return fractions.Fraction(math.pi) * max([cache[K][i] for i in xrange(N)
                          if cache[K][i] is not None])


T = int(raw_input())

for i in xrange(T):
    N, K = [int(x) for x in raw_input().split()]
    pancs = []
    for j in xrange(N):
        pancs.append([int(x) for x in raw_input().split()])

    pancs.sort(reverse=True)

    print 'Case #%d: %.9f' % (i + 1, solve(pancs, N, K))
