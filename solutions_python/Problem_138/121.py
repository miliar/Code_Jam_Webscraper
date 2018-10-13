fin=open("D-large.in","r")
fout=open("OutputD.out","w")

T=int(fin.readline())
Ans=""
for t in range(T):
    n=int(fin.readline())
    X=list(map(float,fin.readline().split()))
    Y=list(map(float,fin.readline().split()))
    X.sort()
    Y.sort()
    D=0
    W=0
    Taken=[False]*n
    minn=0
    for i in range(n-1,-1,-1):
        x=X[i]
        v=-1
        for j in range(n):
            if(Taken[j]):
                continue
            if(Y[j]>x):
                v=Y[j]
                Taken[j]=True
                break
        if(v==-1):
            for z in range(n):
                if(not Taken[z]):
                    Taken[z]=True
                    break
            W+=1
    Taken=[False]*n
    ind=n-1
    best=0
    minn=0
    for i in range(n):
        if(X[i]>Y[minn]):
            minn+=1
            best+=1
        
    Ans+="Case #"+str(t+1)+": "+str(best)+" "+str(W)+"\n"
fout.write(Ans)
fout.close()
