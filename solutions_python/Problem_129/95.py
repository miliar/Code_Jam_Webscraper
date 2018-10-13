MOD = 1000002013


def f(n):
    return (n * n + n - 2) / 2 % MOD


def solve():
    a = []
    d = {}
    s = 0
    for i in xrange(m):
        d[o[i]] = d.get(o[i], 0) + p[i]
        d[e[i]] = d.get(e[i], 0) - p[i]
        s += (f(n) - f(n - (e[i] - o[i]))) * p[i]
    a = d.items()
    a.sort()
    a[0] = [a[0][0], a[0][1]]
    for i in xrange(1, len(a)):
        a[i] = [a[i][0], a[i][1] + a[i - 1][1]]
    r = 0
    for i in xrange(len(a)):
        while a[i][1] > 0:
            q = i
            v = a[i][1]
            while q < n and a[q][1] > 0:
                v = min(v, a[q][1])
                q += 1
            qq = i
            while qq < q and a[qq][1] > 0:
                a[qq][1] -= v
                qq += 1
            r += (f(n) - f(n - (a[q][0] - a[i][0]))) * v
    return (s - r) % MOD


if __name__ == '__main__':
    T = input()
    for t in xrange(T):
        n, m = map(int, raw_input().split())
        o = [0] * m
        e = [0] * m
        p = [0] * m
        for i in xrange(m):
            l, r, k = map(int, raw_input().split())
            o[i] = l - 1
            e[i] = r - 1
            p[i] = k
        print 'Case #{0}: {1}'.format(t + 1, solve())
