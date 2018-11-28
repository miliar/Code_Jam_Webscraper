import sys, itertools, collections
sys.setrecursionlimit(10000)

read_ints = lambda: map(int, raw_input().split())
read_int  = input

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ch = '^>v<'

for no_t in xrange(1, read_int() + 1):
    n, m = read_ints()
    a = [raw_input() for _ in xrange(n)]

    ans = 0
    imp = False  # impossible
    for i in xrange(n):
        for j in xrange(m):
            if a[i][j] == '.':
                continue

            add = None
            for k, c in enumerate(ch):
                grids = [
                    a[i + dx[k] * s][j + dy[k] * s]
                    for s in xrange(1, 101)
                    if 0 <= i + dx[k] * s < n and
                       0 <= j + dy[k] * s < m
                ]
                if len(filter(lambda x: x in ch, grids)):
                    temp = int(a[i][j] != c)
                    if add is None:
                        add = temp
                    else:
                        add = min(add, temp)

            if add is None:
                imp = True
            else:
                ans += add

    if imp:
        ans = 'IMPOSSIBLE'

    print 'Case #%d: %s' % (no_t, ans)
