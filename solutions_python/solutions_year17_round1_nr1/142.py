def work():
    n, m = map(int, input().split())
    g = [list(input()) for _ in range(n)]

    cum_sum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            cum_sum[i + 1][j + 1] = cum_sum[i][j + 1] + cum_sum[i + 1][j] - cum_sum[i][j] + (g[i][j] != '?')

    def cnt(i0, j0, i1, j1):
        return cum_sum[i1][j1] - cum_sum[i0][j1] - cum_sum[i1][j0] + cum_sum[i0][j0]

    def rec(i0, j0, i1, j1):
        tot = cnt(i0, j0, i1, j1)

        for i in range(i0 + 1, i1):
            if 0 < cnt(i0, j0, i, j1) < tot:
                rec(i0, j0, i, j1)
                rec(i, j0, i1, j1)
                return

        for j in range(j0 + 1, j1):
            if 0 < cnt(i0, j0, i1, j) < tot:
                rec(i0, j0, i1, j)
                rec(i0, j, i1, j1)
                return

        c = next(g[i][j] for j in range(j0, j1) for i in range(i0, i1) if g[i][j] != '?')
        for i in range(i0, i1):
            for j in range(j0, j1):
                g[i][j] = c


    rec(0, 0, n, m)
    return g


for i in range(int(input())):
    print('Case #{}:'.format(i + 1))
    print('\n'.join(''.join(l) for l in work()))
