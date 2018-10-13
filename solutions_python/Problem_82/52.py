inf = open("b.in", "r")
ouf = open("b.out", "w")
T = int(inf.readline())
for t in xrange(T):
    print >> ouf, "Case #" + str(t + 1) + ":",
    [k, d] = [int(i) for i in inf.readline().split()]
    x = [0 for i in xrange(k)]
    n = [0 for i in xrange(k)]
    for i in xrange(k):
        [x[i], n[i]] = [int(j) for j in inf.readline().split()]

    INF = 1e15
    l = 0.0
    r = INF
    while r - l > 1e-7:
        m = (l + r) / 2
        can = 1
        lb = -INF
        t = m
        
        for i in xrange(k):
            lm = max(lb, x[i] - t)
            rm = lm + (n[i] - 1) * d
            if rm - x[i] > t:
                can = 0
                break
            lb = rm + d
        if can:
            r = m
        else:
            l = m
    
    print >> ouf, l
inf.close()
ouf.close()    

