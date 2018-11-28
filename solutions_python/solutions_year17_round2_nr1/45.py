from fractions import Fraction


def solve(t):
    D, N = map(int, raw_input().split())
    KS = [map(int, raw_input().split()) for _ in xrange(N)]
    a = -1
    for k, s in KS:
        b = Fraction(D-k, s)
        a = max(a, b)
    print "Case #%d: %.9f" % (t, float(Fraction(D, a)))

T = int(raw_input())
for t in xrange(1, T+1):
    solve(t)
