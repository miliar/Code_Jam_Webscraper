from __future__ import division
from math import factorial as fact
s = [1, 0]
def subfact (n):
    for i in xrange (len(s), n+1):
        s.append((i-1) * (s[-1] + s[-2]))
    return s[n]
p = lambda n, k: subfact(k) / fact(n-k) / fact(k)

T = input()
for i in xrange(T):
    N = input()
    a = map(int, raw_input().split())
    count = 0
    for j, e in enumerate(sorted(a)):
        if a[j] != e:
            count += 1
    exps = [0, 0]
    for n in xrange (2, count+1):
        tot = p(n, n)
        for k in xrange(0, n):
            tot += p(n, k) * (1 + exps[k])
        tot /= (1 - p(n, n))
        exps.append(tot)
    print "Case #%d: %.6f" % (i + 1, exps[-1])