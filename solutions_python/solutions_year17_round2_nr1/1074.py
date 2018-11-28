T = int(raw_input())
for i in xrange(1, T+1):
    D, N = [int(x) for x in raw_input().split()]
    K = []
    S = []
    for _ in xrange(N):
        k, s = [float(x) for x in raw_input().split()]
        K.append(k)
        S.append(s)
    T = [(D-K[j])/S[j] for j in xrange(N)]
    print "Case #{}: {:f}".format(i, D/max(T))
