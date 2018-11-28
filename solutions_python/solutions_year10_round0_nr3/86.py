from sys import stdin

C = int(stdin.readline().strip())
for _ in xrange(1,C+1):
    r,k,n = map(int,stdin.readline().strip().split())
    g = map(int,stdin.readline().strip().split())
    rr=0
    w=0
    e=0
    ex={}
    rx={}
    rx[w] = rr
    ex[w] = e
    while rr < r:
        f=0
        sw = w
        while True:
            f += g[w]
            if f > k: break
            e += g[w]
            w = (w+1)%n
            if w == sw: break
        rr += 1
        if w in rx: 
            crr = rr - rx[w]
            ct = (r - rx[w]) / crr
            e = ex[w] + (e - ex[w])*ct
            rr = rx[w] + (rr - rx[w])*ct
            break
        rx[w] = rr
        ex[w] = e

    while rr < r:
        f=0
        sw = w
        while True:
            f += g[w]
            if f > k: break
            e += g[w]
            w = (w+1)%n
            if w == sw: break
        rr += 1
    print "Case #%d: %d"%(_,e)
