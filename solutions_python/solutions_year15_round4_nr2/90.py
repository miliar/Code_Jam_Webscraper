eps = 1e-9
T = int(raw_input())
for C in xrange(1, T+1):
    print "Case #%d:" % C,
    inp = raw_input().split()
    n = int(inp[0])
    v = float(inp[1])
    x = float(inp[2])
    r1, t1 = map(float, raw_input().split())
    if n == 1:
        if abs(t1 - x) >= eps:
            print "IMPOSSIBLE"
        else:
            print "%.7f" % (v / r1)
    else:
        r2, t2 = map(float, raw_input().split())
        if abs(t1 - x) < eps and abs(t2 - x) < eps:
            print "%.7f" % (v / (r1 + r2))
        elif abs(t1 - x) < eps:
            print "%.7f" % (v / r1)
        elif abs(t2 - x) < eps:
            print "%.7f" % (v / r2)
        elif t1 - eps > x and t2 - eps > x:
            print "IMPOSSIBLE"
        elif t1 + eps < x and t2 + eps < x:
            print "IMPOSSIBLE"
        else:
            t = v*(x - t1) / (t2*r2 - t1*r2)
            tt = (v - t*r2)/r1
            print "%.7f" % (max(t, tt))
