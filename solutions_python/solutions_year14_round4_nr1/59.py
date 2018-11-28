t = int(raw_input())
for T in xrange(1,t+1):
    n, x = [int(i) for i in raw_input().split()]
    s = sorted([int(i) for i in raw_input().split()])
    c = [s[-1]]
    for i in xrange(n-2,-1,-1):
        f = False
        for j in xrange(len(c)):
            if c[j]+s[i] <= x:
                c[j] = 90019001
                f = True
                break
        if not f:
            c.append(s[i])
    print "Case #{0}: {1}".format(T, len(c))