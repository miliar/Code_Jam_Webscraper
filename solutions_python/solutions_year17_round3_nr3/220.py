
from sys import setrecursionlimit
setrecursionlimit(10000)

NINF = -10**18


def solve(t):
    N, K = map(int, raw_input().split())
    U = float(raw_input())
    Praw = raw_input().split()
    Ps = []
    for pr in Praw:
        if pr == '1.0000':
            Ps.append(1.0)
        else:
            Ps.append(int(pr[2:])/10000.0)

    while U > 1e-12 and sum(Ps) < N:
        Ps.sort()

        min_p = Ps[0]
        count = Ps.count(min_p)

        # print Ps, U

        next_p = 1.0
        for p in Ps:
            if p > min_p:
                next_p = p
                break
        diff = next_p - min_p

        u = min(diff, U / count)
        # print 'min_p=%s, count=%s, diff=%s, u=%s' % (min_p, count, diff, u)

        for i, p in enumerate(Ps):
            if p > min_p:
                break
            Ps[i] += u
            U -= u

    ans = 1.0
    for p in Ps:
        ans *= p

    print 'Case #%d: %.12f' % (t, ans)

T = input()
for i in xrange(T):
    solve(i+1)
