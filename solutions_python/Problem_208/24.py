import sys, itertools, collections
sys.setrecursionlimit(10000)

read_ints = lambda: map(int, raw_input().split())
read_int  = input

INF = 10**100

for no_t in xrange(1, read_int() + 1):
    n, q = read_ints()
    es = [read_ints() for _ in xrange(n)]
    e = [e for e, _ in es]
    s = [s for _, s in es]

    d = [read_ints() for _ in xrange(n)]

    dist = [-1] + [d[i-1][i] for i in xrange(1, n)]
    #print(dist)

    ans = []
    for qq in xrange(q):
        u, v = read_ints()
        assert u == 1 and v == n
        dp = [INF] * n
        dp[0] = 0

        for i in xrange(n):
            c = 0
            for j in xrange(i + 1, n):
                c += dist[j]
                if e[i] < c:
                    break
                dp[j] = min(dp[j], dp[i] + 1.0 * c / s[i])

        ans.append(dp[n - 1])
    ans = ''.join(map(str, ans))
    print 'Case #%d: %s' % (no_t, ans)
