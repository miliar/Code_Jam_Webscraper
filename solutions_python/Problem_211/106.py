T = int(raw_input())

def solve():
    n = int(raw_input().split()[0])  # n == k
    u = float(raw_input())
    p = sorted(map(float, raw_input().split()), key=lambda x: -x)
    uu = u + sum(p)
    if uu >= n:
        return 1.0
    cur = 1.0
    for i in xrange(len(p)):
        if p[i] > uu / (n - i):
            uu -= p[i]
            cur *= p[i]
        else:
            return cur * (uu / (n - i)) ** (n - i)

for t in xrange(T):
    print 'Case #%s: %.9f' % (t+1, solve())
