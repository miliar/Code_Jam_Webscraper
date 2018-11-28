def solve():
    d, n = map(int, raw_input().split())
    gt = 0
    for _ in xrange(n):
        k, s = map(int, raw_input().split())
        tt = 1.0 * (d - k) / s
        if gt < tt:
            gt = tt
    return d / gt

T = int(raw_input())
for t in xrange(T):
    print "Case #%d: %.12f" % (t + 1, solve())
