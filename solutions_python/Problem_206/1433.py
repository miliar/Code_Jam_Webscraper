def sol(d, n, H):
    for i in range(n-2,-1,-1):
        R = []
        for j in range(n-1,i,-1):
            s = (d-H[i][0])/(d - H[j][0]) * H[j][1]
            R.append(s)
        H[i] = (H[i][0],min(min(R),H[i][1]))
    RR = []
    for i in range(n):
        s = d/(d - H[i][0]) * H[i][1]
        RR.append(s)
    return min(RR)


t = int(raw_input().strip())
for a0 in xrange(t):
    d, n  = map(int,raw_input().strip().split(" "))
    H = []
    for b0 in range(n):
        k, s  = map(float,raw_input().strip().split(" "))
        H.append((k,s))
    H_sorted = sorted(H, key=lambda tup: tup[0])
    print "Case #%d: %.6f" % (a0+1,sol(d,n,H_sorted))
