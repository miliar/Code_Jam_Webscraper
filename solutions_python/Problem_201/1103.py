T = int(raw_input())
for t in xrange(T):
    f = raw_input().split()
    N = int(f[0])
    K = int(f[1])
    stall = {}
    stall[N] = 1
    while True:
        n = max(stall.keys())
        x = int(n/2)
        y = int((n-1)/2)
        if K <= 1:
            break
        z = 1
        if stall[n] < K:
            z = stall[n]
        stall[n] -= z
        K -= z
        if stall[n] == 0:
            del stall[n]
        if x not in stall:
            stall[x] = 0
        if y not in stall:
            stall[y] = 0
        stall[x] += z
        stall[y] += z
    print "Case #%d: %d %d" % (t+1, x, y)
