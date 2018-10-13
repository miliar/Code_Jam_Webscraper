import math
goin=open("A.in","r")
t=int(goin.readline().strip())
outs=list()



for i in range(t):
    xd=goin.readline().strip().split()
    n=int(xd[0])
    k=int(xd[1])
    panc=list()
    for j in range(n):
        lol=list(map(int, goin.readline().strip().split())) #R,H
        S=math.pi*lol[0]*lol[0]
        KS=2*math.pi*lol[0]*lol[1]
        X=S+KS
        lol.append(S)
        lol.append(KS)
        lol.append(X)
        panc.append(lol)
    panc=sorted(panc, key = lambda x: x[3],reverse=True)
    sol=panc[:k]
    nosol=panc[k:]
    sol2=sorted(sol, key = lambda x: x[2], reverse=True)
    maksiX=sol2[0][2]+sol[-1][3]
    for pann in nosol:
        if pann[4]>maksiX:
            maksiX=pann[4]
    ans=0
    for j in range(k):
        ans+=sol[j][3]
    ans-=sol[-1][3]
    ans+=maksiX
    outt="Case #"+str(i+1)+": "+str(ans)+"\n"
    outs.append(outt)
goin.close()



goout=open("A.out","w")
for i in range(t):
    goout.write(outs[i])
goout.close()
