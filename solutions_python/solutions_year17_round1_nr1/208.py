t = input()
for cas in xrange(t):
    r, c = map(int, raw_input().split())
    g = [list(raw_input()) for _ in xrange(r)]

    res = [[''] * c for _ in xrange(r)]
    for i in xrange(r):
        for j in xrange(c):
            if g[i][j] == '?':
                continue
            res[i][j] = g[i][j]
            k = j + 1
            while k < c and g[i][k] == '?':
                res[i][k] = g[i][j]
                k += 1

            k = j - 1
            while k >= 0 and g[i][k] == '?':
                res[i][k] = g[i][j]
                k -= 1

    for i in xrange(r):
        if res[i].count('') == c:
            continue
        k = i + 1
        while k < r and res[k].count('') == c:
            res[k] = res[i]
            k += 1

    for i in reversed(xrange(r)):
        if res[i].count('') == c:
            continue
        k = i - 1
        while k >= 0 and res[k].count('') == c:
            res[k] = res[i]
            k -= 1

    print 'Case #{0}:'.format(cas+1)
    for row in res:
        print ''.join(row)
