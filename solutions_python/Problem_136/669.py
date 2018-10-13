t = int(raw_input())

for case in xrange(t):
    c, f, x = map(float, raw_input().split())
    t1 = 0
    k1 = 2
    t2 = c/2
    k2 = 2 + f
    while True:
        if k1 * k2 * (t1 - t2) / (k1 - k2) < x:
            t1 = t2
            k1 = k2
            k2 += f
            t2 += c/k1
        else:
            print "Case #%d: %.8f" % (case + 1, t1 + x / k1)
            break

