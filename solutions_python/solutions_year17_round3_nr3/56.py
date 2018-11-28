import fractions

T = int(raw_input())

for i in xrange(T):
    N, K = [int(x) for x in raw_input().split()]
    U = fractions.Fraction(float(raw_input()))

    Ps = [fractions.Fraction(float(x)) for x in raw_input().split()]

    Ps.sort()
    for j in xrange(1, len(Ps)):
        quota = min(U / j, Ps[j] - Ps[0])
        for k in xrange(j):
            Ps[k] += quota

        U -= quota * j

    if U > 0:
        for j in xrange(len(Ps)):
            Ps[j] += U / N
            Ps[j] = min(Ps[j], 1)

    res = 1
    for p in Ps:
        res *= p

    print 'Case #%d: %.9f' % (i+1, res)
    




