T = int(raw_input())
for n in xrange(1, T + 1):
    D, N = [int(x) for x in raw_input().split(" ")]
    locs = []
    for _ in xrange(N):
        K, S = [float(x) for x in raw_input().split(" ")]
        locs.append((K, S))
    time = max([(D-K)/S for K, S in locs])
    print "Case #{}: {}".format(n, D/time)
