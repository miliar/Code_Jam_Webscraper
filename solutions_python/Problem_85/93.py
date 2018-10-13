T = input()
for caso in range(T):
    line = map(int, raw_input().split())
    L, t, N, C = line[:4]
    a = line[4:]
    
    tot = 0
    dis = list()
    for i in range(N):
        dis.append(0)
    #~print dis
    
    for i in range(N):
        dis[i] = tot
        tot += 2*a[i%C]
    
    res = tot
    #~print dis
    if L == 0:
        pass
    elif L == 1:
        for i in range(N):
            if dis[i]+2*a[i%C] <= t: continue
            dif = max(t-dis[i],0)
            res = min(res, tot-2*a[i%C]+dif+max(0,a[i%C]-dif/2))
    elif L == 2:
        for i in range(N):
            if dis[i]+2*a[i%C] <= t: continue
            dif = max(t-dis[i],0)
            res = min(res, tot-2*a[i%C]+dif+max(0,a[i%C]-dif/2))
            for j in range(i+1, N):
                #~dif1 = max(t-dis[i],0)
                #~if dis[j]-2*a[i%C]+dif1+max(0,a[i%C]-dif1/2)+a[j%C] <= t: continue
                #~dif2 = max(t-2*(dis[j]-2*a[i%C]+dif1+max(0,a[i%C]-dif1/2)),0)
                #~res = min(res, tot-2*a[i%C]+dif1+max(0, a[i%C]-dif1/2)-2*a[j%C]+dif2+max(0,a[j%C]-dif2/2))
                res = min(res, tot-2*a[i%C]+dif+max(0, a[i%C]-dif/2)-a[j%C])
    
    print "Case #%s: %s" % (caso+1, res)
