import math
tot = int(raw_input())
cas = 0
while cas < tot:
    n, m = map(int, raw_input().split())
    ps = map(float, raw_input().split())

    prod = [1]
    logprod = [0]
    for p in ps:
        logprod.append(logprod[-1] + math.log(p))
        prod.append(math.exp(logprod[-1]))

    ans = m * 2
    ans = min(ans, 1 + prod[n] * (m - n) + (1 - prod[n])*(2*m - n + 1))
    for k in xrange(1, n+1):
        ans = min(ans, prod[n-k]*(m-n+k) + (1 - prod[n-k])*(2*m-n+k + 1) + k + 1)
    ans = min(ans, m + 2)
    cas += 1
    print 'Case #%d: %.7f' % (cas, ans)

