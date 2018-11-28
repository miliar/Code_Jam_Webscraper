T=int(raw_input())


for iT in range(T):
    R,k,N = [int(i) for i in raw_input().split()]
    g = [int(i) for i in raw_input().split()]

    nxt=[0]*N
    occEd = [False]*N
    ll = [0]*N
    zC = [0]*N

    cCur = 0
    i=0
    occEd[0] = True
    while True:
        cCur = 0
        i0 = i
        while cCur + g[i] <= k:
            cCur += g[i]
            i = (i + 1) % N
            if  i == i0:
                break
        nxt[i0] = i
        if not occEd[i]:
            occEd[i] = True
            ll[i] = ll[i0] + cCur
            zC[i] = zC[i0] + 1
            #print 'a', zC[i], i
        else:
            tZQ = ll[i0] + cCur - ll[i]
            lzC = zC[i0] + 1 - zC[i]
            pZQ = zC[i]
            #print i
            #print pZQ, tZQ
            #print lzC
            break

    ans = ((R-pZQ)/lzC) * tZQ
    if R-pZQ>=0:
        ans += ll[i]
        sL = (R-pZQ)%lzC
        iNow = i
    else:
        iNow = 0
        sL = R

    i=iNow
    for j in range(sL):
        cCur = 0
        while cCur + g[i] <= k:
            cCur += g[i]
            i = (i + 1) % N
        ans += cCur


    print "Case #%d: %d" %(iT+1, ans)

