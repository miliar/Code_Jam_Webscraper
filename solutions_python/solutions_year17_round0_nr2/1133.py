def tidy(x):
    l = str(x)
    k = ""
    for c in l:
        nc = c
        if k and nc < k[-1]:
            nc = k[-1]
        k += nc
    return int(k)
    
T = int(raw_input())
for t in xrange(T):
    f = raw_input().split()
    N = int(f[0])
    if N == tidy(N):
        print "Case #%d: %d" % (t+1, N)
        continue
    x = 0
    y = 1
    while y < N:
        z = tidy(N-y)
        if z < N:
            x = z
            break
        y *= 2
    while x < N:
        y = x
        x = tidy(x+1)
    print "Case #%d: %d" % (t+1, y)
