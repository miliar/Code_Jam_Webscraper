def ans(t, x):
    if x % 2 == 1:
        print "Case #%d: %d %d" % (t+1, x / 2, x / 2)
    else:
        print "Case #%d: %d %d" % (t+1, x / 2, x / 2 - 1)

T = int(raw_input())

for t in xrange(T):
    N, K = map(int, raw_input().split())
    x, P, L = N, 1, 0

    while K > 0:
        if L >= K:
            ans(t, x+1)
            break
        if P + L >= K:
            ans(t, x)
            break
        # Not yet
        if x % 2 == 0:
            x, P, L, K = x/2 - 1, P, P + 2*L, K - P - L
        else:
            x, P, L, K = x/2, 2*P + L, L, K - P - L
