def solve():
    n, q = map(int, raw_input().split())
    dat = [map(int, raw_input().split()) for _ in xrange(n)]
    d = [map(int, raw_input().split()) for _ in xrange(n)]
    for i in xrange(n):
        d[i][i] = 0
    for k in xrange(n):
        for i in xrange(n):
            for j in xrange(n):
                if d[i][k] == -1 or d[k][j] == -1:
                    continue
                if d[i][j] == -1 or d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
    ans = []
    for _ in xrange(q):
        u, v = map(int, raw_input().split())
        u, v = u - 1, v - 1
        dd = [1e12] * n
        dd[u] = 0
        rest = set(xrange(n))
        for i in xrange(n):
            j = min(rest, key=lambda x: dd[x])
            rest.remove(j)
            for k in xrange(n):
                if d[j][k] != -1 and d[j][k] <= dat[j][0]:
                    td = dd[j] + 1.0 * d[j][k] / dat[j][1]
                    if dd[k] > td:
                        dd[k] = td
        ans.append(dd[v])
    print ' '.join("%.12f" % x for x in ans)

T = int(raw_input())
for t in xrange(T):
    print "Case #%d:" % (t + 1),
    solve()
