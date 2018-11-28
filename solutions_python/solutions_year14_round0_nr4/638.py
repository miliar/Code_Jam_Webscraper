import bisect


ri = lambda: int(raw_input())
rii = lambda: map(int, raw_input().split())
rff = lambda: map(float, raw_input().split())


def war(c, n, k):
    p = 0
    for x in n:
        if k[-1] > x:
            i = bisect.bisect(k, x)
            k.pop(i)
        else:
            # remove ken' smallest block
            k = k[1:]
            p += 1
    return p


def d_war(c, n, k):
    p = 0
    # n's smallest for k's biggest
    i = bisect.bisect(n, k[0])
    if i:
        n = n[i:]
        k = k[:-i]
    ki = ni = 0
    kl = nl = c - i
    while ki < kl and ni < nl:
        if k[ki] < n[ni]:
            p += 1
            ki += 1
            ni += 1
        else:
            ni += 1
            kl -= 1
    return p


def solve(t, c, n, k):
    n.sort()
    k.sort()
    print "CASE #%d: %d %d" % (t,
                               d_war(c, n[:], k[:]),
                               war(c, n[:], k[:]))


tn = ri()
for t_ in xrange(1, tn + 1):
    c_ = ri()
    n_ = rff()
    k_ = rff()
    solve(t_, c_, n_, k_)
