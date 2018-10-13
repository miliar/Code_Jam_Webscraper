#!/usr/bin/python

import sys

f = open(sys.argv[1])
cnt = int(f.readline())


for i in range(0,cnt):
    R, k, N = [int(x) for x in f.readline().split()]
    g = [int(x) for x in f.readline().split()]

    def get_next(g, gi):
        cnt, dlr, init_gi = 0, 0, gi
        while dlr + g[gi] <= k:
            dlr += g[gi]
            gi += 1
            if gi == N:
                gi = 0
                break
        while dlr + g[gi] <= k and gi < init_gi:
            dlr += g[gi]
            gi += 1
            if gi == N:
                gi = 0
                break
        return gi, dlr

    # if i == 9:
    #     print R, k, N
    #     print g
    # else:
    #     continue

    r, gi, total = 0, 0, 0
    while r < R:
        gi, dlr = get_next(g, gi)
        total += dlr
        r += 1
        # if gi == 0:             # we have done a complete cycle.
        #     rep = R/r
        #     if R%r == 0:
        #         r = R
        #     else:
        #         r = (R-r) + (R%r)
        #     print rep, r, R-r, R%r
        #     r += (rep-1)
        #     total = total*rep
            
    print "Case #"+str(i+1)+": "+str(total)
    
