
for case in range(input()):
    print "Case #"+str(case+1)+":",
    (M,V)=map(int,raw_input().split())
    G=[False]*(M+1)
    C=[False]*(M+1)
    val=[False]*(M+1)
    mc=[-1]*(M+1)
    for i in range(1,(M-1)/2+1):
        (G[i],C[i])=map(bool,map(int,raw_input().split()))
    for i in range((M+1)/2):
        val[(M-1)/2+1+i]=bool(int(input()))
    for i in range((M-1)/2,0,-1):
        orv=(val[2*i] or val[2*i+1])
        andv=(val[2*i] and val[2*i+1])
        if G[i]: val[i]=andv
        else: val[i]=orv
        #print "val",val[i],G[i],val[2*i],val[2*i+1]
        chcost=[M+1]*8
        mincost=M+1
        ind=-1
        for j in range(8):
            ch=[bool((j/4)%2),bool((j/2)%2),bool(j%2)]
            if ch[0]: v1=val[2*i]
            else: v1=(not val[2*i])
            if ch[1]: v2=val[2*i+1]
            else: v2=(not val[2*i+1])
            if ch[2]: v3=G[i]
            else: v3=(not G[i])
            if v3: vee=(v1 and v2)
            else: vee=(v1 or v2)
            #if i==1: print "vee",vee,val[i],val[2*i],val[2*i+1],vee==val[i],ch,G[i],v1,v2,v3,ch[2],C[i]
            if not (vee==val[i]):
                if not ((ch[0] or C[2*i]) and (ch[1] or C[2*i+1]) and (ch[2] or C[i])): continue
                cost=0
                if (not ch[0]) and C[2*i]: cost=cost+mc[2*i]
                if (not ch[1]) and C[2*i+1]: cost=cost+mc[2*i+1]
                if (not ch[2]) and C[i]: cost=cost+1
                #print "cost",i,j,cost
                if cost<mincost:
                    mincost=cost
                    ind=j
        if mincost<M+1:
            mc[i]=mincost
            C[i]=True
        else: C[i]=False
    #print mc
    #print val
    if val[1]==V:
        print 0
    elif mc[1]==-1:
        print "IMPOSSIBLE"
    else:
        print mc[1]
