for t in xrange(int(raw_input())):
    N, K = [int(i) for i in raw_input().split()]
    print "Case #%d: %s" % (t+1, 'ON' if K%2**N==2**N-1 else 'OFF')
