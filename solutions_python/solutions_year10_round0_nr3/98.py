import re,sys

fi=open("C-large.in")#"C-small-attempt0.in")


sys.stdout=open("C.out","w")
T=int(fi.readline())
for t in range(T):
    R,k,N=map(int,re.sub("\s+$", "", fi.readline()).split())
    G=map(int,re.sub("\s+$", "", fi.readline()).split())
#    print R,k,N
#    print G
    ern=[0 for i in range(N)]
    brk=[0 for i in range(N)]
    ern[-1]=G[-1]
    for j in range(N):
        ern[j]=ern[j-1]-G[j-1]
        for i in range(N):
            p=(i+brk[j-1])%N
            ern[j]+=G[p]
            if ern[j]>k:
                ern[j]-=G[p]
                brk[j]=p
                break
    p=0
    ans=0
    hist=[]
    hern=[]
    while True:
        ans+=ern[p]
        if p in hist:
            break
        else:
            hist.append(p)
            hern.append(ans)
        p=brk[p]
    entered=hist.index(p)
    loop_ern=hern[-1]
    if entered-1>=0:
        loop_ern-=hern[entered-1]
    loop_len=len(hern)-entered
    
    pre=hern[:entered]
    post=hern[entered:]
    if len(pre)>0:
        post=[pi-pre[-1] for pi in post]
#    print hern,entered,loop_len,loop_ern
#    print pre
#    print post
    
    ans=0
    if len(pre)>0 and R>0:
        if R<=len(pre):
            ans=pre[R-1]
        else:
            ans=pre[-1]
    R=max(0,R-len(pre))
    ans+=(R/loop_len)*loop_ern
    R%=loop_len
    if R>0:
        ans+=post[R-1]
    print "Case #%i: %s"%(t+1,ans)
