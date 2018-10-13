# coding: utf-8

tcase = input()
for t in range(tcase):
    r,k,n = map(int, raw_input().split(" "))
    g = map(int, raw_input().split(" "))
    #print r,k,n,g
    earn = 0
    i = 0
    for j in range(r):
        #print i,g[i:]
        p = 0
        x = i
        while True:
            p += g[i]
            i = (i + 1) % n
            if p >= k or i == x:
                if p > k:
                    i = (i - 1) % n
                    p -= g[i]
                break
        #print j,p
        earn += p
    print "Case #%d: %d" % (t + 1, earn)
