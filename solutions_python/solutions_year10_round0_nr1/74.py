T = int(raw_input())

for t in xrange(T):
    (N, K) = map(int, raw_input().split(' '))
    off = bool((K+1)%(2**N))

    print "Case #%d: %s" % (t+1, off and "OFF" or "ON")
