def solve(r, c, m):
    f = [['*'] * c for _ in xrange(r)]
    if m == 0:
        return [['.'] * c for _ in xrange(r)]
    l = r * c - m
    if l == 1:
        return f
    if r == 1:
        return [['.'] * l + ['*'] * m]
    for i in xrange(2, r+1):
        for j in xrange(2, c+1):
            if i * j == l:
                for ii in xrange(i):
                    for jj in xrange(j):
                        f[ii][jj] = '.'
                return f
    for i in xrange(2, r):
        for j in xrange(2, c):
            for k in xrange(2, i + 1):
                kk = l - (i * j + k)
                if kk < 0 or kk == 1 or kk > j:
                    continue

                for ii in xrange(i):
                    for jj in xrange(j):
                        f[ii][jj] = '.'

                for ii in xrange(k):
                    f[ii][j] = '.'

                for jj in xrange(kk):
                    f[i][jj] = '.'

                return f
    return None


t = input()
for nt in xrange(1, t + 1):
    print 'Case #%d:' % nt
    r, c, m = map(int, raw_input().split())
    f = solve(r, c, m)
    if f:
        f[0][0] = 'c'
    if f is None:
        f = solve(c, r, m)
        if f:
            f[0][0] = 'c'
            f = zip(*f)
    if f is None:
        print 'Impossible'
    else:
        f = [''.join(x) for x in f]
        print '\n'.join(f)
