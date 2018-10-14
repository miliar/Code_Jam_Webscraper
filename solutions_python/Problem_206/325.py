def main(index):
    print 'Case #%d:' % index,
    D, N = map(float, raw_input().split())
    Hs = [map(float, raw_input().split()) for i in xrange(int(N))]
    ATs = [(D-K)/S for K, S in Hs]
    t = max(ATs)
    print '%.6f' % (D/t, )

T = int(raw_input())
for i in xrange(1, T+1):
    main(i)
