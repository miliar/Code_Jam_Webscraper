#!/usr/bin/env python

T = input()

for t in xrange(T):
    C, F, X = map(float, raw_input().split())
    f = lambda n: X/(2+n*F) + C*sum([1/(2+i*F) for i in xrange(n)])
    j, fmin = 1, f(0)
    while True:
        fj = f(j)
        if fj < fmin:
            fmin = fj
            j = j + 1
        else:
            break
    print 'Case #%d: %.10f' % (t+1, fmin)

