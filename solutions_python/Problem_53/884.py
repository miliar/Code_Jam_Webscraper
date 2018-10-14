T = input()
for case in xrange(1,T+1):
    N,K = map(int,raw_input().split())
    print "Case #%s: %s" % (case, 'ON' if (K + 1) % (1 << N) == 0 else 'OFF')
