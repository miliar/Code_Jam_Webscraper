T = int(raw_input())
for t in xrange(1, T+1):
    N, K = map(int, raw_input().split())
    l = len('{0:b}'.format(K)) - 1
    b = 1 << l
    x = (N - b + 1) / b
    y = (N - b + 1) % b
    c = x
    if K - b < y:
        c += 1
    print 'Case #%d: %d %d' % (t, c/2, (c-1)/2)
