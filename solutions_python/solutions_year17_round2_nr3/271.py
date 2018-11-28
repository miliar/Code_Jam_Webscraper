INF = 10 ** 100
class Solution(object):
    def __init__(self, n, q, es, g, qs):
        self.n = n
        self.q = q
        self.es = es
        self.g = g
        self.qs = qs

    def solve(self):
        assert len(self.qs) == 1
        (qa, qb) = self.qs[0]

        self.dp = [INF for i in xrange(n)]
        self.dis = [0 for i in xrange(n)]

        for i in xrange(n - 1):
            (next, dis) = g[i][0]
            self.dis[i + 1] = self.dis[i] + dis

        self.dp[0] = 0
        for i in xrange(1, n):
            for j in xrange(i):
                dd = self.dis[i] - self.dis[j]
                hs, hv = es[j]
                if dd <= hs:
                    self.dp[i] = min(self.dp[i], self.dp[j] + 1.0 * dd / hv)
        return self.dp[n - 1]

if __name__ == '__main__':
    T = int(raw_input())
    for case_ in xrange(T):
        print 'Case #%d:' % (case_ + 1),
        (n, q) = map(int, raw_input().split())
        g = [[] for i in xrange(n)]

        es = []
        for i in xrange(n):
            (a, b) = map(int, raw_input().split())
            es.append((a, b))

        for i in xrange(n):
            ns = map(int, raw_input().split())
            for j in xrange(n):
                if ns[j] != -1:
                    assert j == i + 1
                    g[i].append((j, ns[j]))

        qs = []
        for i in xrange(q):
            (a, b) = map(int, raw_input().split())
            qs.append((a - 1, b - 1))

        print Solution(n, q, es, g, qs).solve()
