T = int(raw_input())
for t in xrange(1, T + 1):
    D, N = map(int, raw_input().split(' '))

    Vs = []
    for n in xrange(N):
        K, S = map(float, raw_input().split(' '))
        Vs.append(D * S / (D - K))

    print 'Case #{}: {}'.format(t, min(Vs))
