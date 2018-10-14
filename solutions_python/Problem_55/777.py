def coaster(r, k, g):
    m = 0
    d = len(g)
    for i in range(r):
        t = 0
        c = 0
        while t < k and c < d:
            if t +g[c] <= k:
                t += g[c]
            else:
                break
            c += 1
        m += t
        g = g[c:] + g[:c]
    return m
f = open("C-small-attempt0.in","r")
o = open("Cout.out","w")
for i in range(int(f.readline().rstrip())):
    d = map(int,f.readline().rstrip().split())
    s = "Case #%d: %d \n" % (i+1, coaster(d[0],d[1],map(int,f.readline().rstrip().split())))
    print s
    o.write(s)
    
