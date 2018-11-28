for i in xrange(int(raw_input())):
    n,k = (int(x) for x in raw_input().split())
    cycle = 2 << (n-1) if n else 1
    if (k+1) % cycle: print "Case #%d: OFF" % (i+1)
    else: print "Case #%d: ON" % (i+1)
