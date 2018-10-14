T = int(raw_input())


for i in range(T):
    R, k ,N = map(int, raw_input().split())
    g = map(int, raw_input().split())
    
    #print R, k, N
    #print g
    earn = 0
    pos = 0
    s = sum(g)
    t, tmp = 0, 0
    while t < R:
        #print t
        if tmp + g[pos] <= k and tmp < s:
            tmp += g[pos]
            pos = (pos+1) % N
        else:
            earn += tmp
            tmp = 0
            t+=1
    print "Case #%d: %d" % (i+1, earn)
    