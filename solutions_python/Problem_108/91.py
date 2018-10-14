def solve(v, d):
    nv = len(v)
    cache = {}
    def _solve(x, i):
        'Can we get to d from pos x, holding vine i?'
        if (x, i) not in cache:
            cache[(x,i)] = 0
            s = v[i][0]-x
            e = x + 2*s
            if e >= d: cache[(x,i)] = 1
            for j in range(i+1, nv):
                if v[j][0] <= e:
                    y = max(v[i][0], v[j][0]-v[j][1])
                    if _solve(y, j):
                        cache[(x,i)] = 1
                        break
        return cache[(x,i)]
    return _solve(0, 0)

rd = raw_input
for t in range(1, 1+int(rd())):
    v = int(rd())
    print 'Case #%d: %s' % (
        t, ['NO', 'YES'][solve([map(int, rd().split()) for _ in range(v)], int(rd()))])

