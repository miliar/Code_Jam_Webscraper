t = int(raw_input())

for i in xrange(1, t + 1):
    d, n = [int(a) for a in raw_input().split(" ")]
    k = [0 for a in xrange(n)]
    s = [0 for a in xrange(n)]
    t = [0.0 for a in xrange(n)]
    for j in xrange(n):
        k[j], s[j] = [int(a) for a in raw_input().split(" ")]
        t[j] = float(d - k[j]) / s[j]

    print "Case #{}: {}".format(i, float(d) / max(t))
