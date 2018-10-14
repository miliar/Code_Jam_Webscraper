
def solve(D, N, k, s):
    diffrate = []
    for i in xrange(len(k)):
        x = (D - k[i])/s[i]
        if x > 0:
            diffrate.append(x)
    diffrate.sort()
    return D / diffrate[-1]

g = open('a.out', 'w')
with open('alarge.in', 'r') as f:
    T = int(f.readline())
    for c in xrange(T):
        D, N = map(int, f.readline().split())
        k = []
        s = []
        for _ in xrange(N):
            a, b = map(float, f.readline().split())
            k.append(a)
            s.append(b)
        r = solve(D, N, k, s)
        print 'Case #%s: %.6f' % (c + 1, r)
        g.write('Case #%s: %.6f\n' % (c + 1, r))
