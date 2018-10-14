f = open("D-large.in")
fout = open("D.out", "w")

T = int(f.readline())
for t in xrange(T):
    N = int(f.readline())
    a = map(lambda x: int(x)-1, f.readline().split())

    r = 0
    for i in xrange(N-1):
        if a[i] != i:
            r += 1
            while a[i] != i:
                j = a[i]
                a[i] = a[j]
                a[j] = j
                r += 1
    
    print >>fout, "Case #%d: %f" % (t+1, r)
    