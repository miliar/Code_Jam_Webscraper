out=open("out2.txt","w")
from itertools import *
T=int(input())
#print T
pi=float(3.14159265358979)
for case in range(T):
    N,K=map(int,raw_input().split())
    P=[]
    Rmax=0
    Rind=0
    for i in range(N):            
        R,H=map(int,raw_input().split())
        P.append([i,R,H,2*R*H])
        if R>Rmax:
            Rmax=R
            Rind=i
            Hmax=H
    print P
    st=[i for i in xrange(N)]
    
    ans=0
    for c in combinations(st,K):
        sm=0
        Rcm=0
        for i in xrange(K):
            sm+=P[c[i]][3]
            Rcm=max(Rcm,P[c[i]][1])
        sm+=Rcm**2
        ans=max(ans,sm)

    print ans
    out.write("Case #"+str(case+1)+": "+str(ans*pi)+"\n")
    continue        
    P=sorted(P,key=lambda x:-x[3])
    #print P
    ans=0
    Rcm=0
    for i in xrange(K):
        ans+=P[i][3]
        Rcm=max(Rcm,P[i][1])
    ans+=Rcm**2
    P1=sorted(P,key=lambda x:-x[1])
 #   print P1
#    sm+=P1[0][1]**2

    #ans=0
    for i in xrange(K):
        sm=0
        Rcm=0
        for j in xrange(K):
            if i==j:
                sm+=2*Rmax*Hmax
            else:
                sm+=P[j][3]
        sm+=Rmax**2
        ans=max(sm,ans)
#        print sm,ans
        

    print ans
    out.write("Case #"+str(case+1)+": "+str(ans*pi)+"\n")

out.close()