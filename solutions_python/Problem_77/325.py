for t in xrange(input()):
    n = input()
    vs = map(int, raw_input().split())
    print "Case #%d: %d.000000" % (t+1, n-sum(a==b for a, b in zip(vs, sorted(vs))))