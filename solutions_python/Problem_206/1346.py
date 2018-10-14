from __future__ import division
for q in range(1, input() + 1):
    D, N = map(int, raw_input().split())
    m = 0
    for i in range(N):
        k, s = map(int, raw_input().split())
        m = max(m, (D - k) / s)
    print "Case #%s: %s" % (q, D / m)
