import sys

t = int(sys.stdin.readline().strip())

for i in xrange(t):
    d, n = [int(p) for p in sys.stdin.readline().strip().split()]
    k = []
    s = []
    for j in xrange(n):
        ki, si = [int(p) for p in sys.stdin.readline().strip().split()]
        k.append(ki)
        s.append(si)
        
    for jj in xrange(n - 1):
        for kk in xrange(jj + 1, n):
            if k[jj] > k[kk]:
                p = k[jj]
                k[jj] = k[kk]
                k[kk] = p
                p = s[jj]
                s[jj] = s[kk]
                s[kk] = p


    max_arrive_time = None
    for j in xrange(n):
        ind = n - j - 1
        arrive_time = 1.0 * (d - k[ind]) / s[ind]
        if (j == 0) or (arrive_time > max_arrive_time):
            max_arrive_time = arrive_time

    print "Case #%d: %.6f" % (i + 1, 1.0 * d / max_arrive_time)

