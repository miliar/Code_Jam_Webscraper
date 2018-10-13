fin=open("B-large.in","r")
fout=open("OutputDP.out","w")
def Solve(x,a,b,c):
    # a -> Change any bit in A
    # b -> Chnage any bit in B
    # c -> Chnage any bit in C
    if(x==len(A)):
        return 1
    if((x,a,b,c) in Mem):
        return Mem[(x,a,b,c)]
    if(c):
        if(a and b):
            Mem[(x,a,b,c)]= 4*Solve(x+1,True,True,True)
            return Mem[(x,a,b,c)]
        elif(a):
            if(B[x]==1):
                Mem[(x,a,b,c)]= 2*Solve(x+1,True,False,True)+2*Solve(x+1,True,True,True)
                return Mem[(x,a,b,c)]
            else:
                Mem[(x,a,b,c)]= 2*Solve(x+1,True,False,True)
                return Mem[(x,a,b,c)]
        elif(b):
            if(A[x]==1):
                Mem[(x,a,b,c)]= 2*Solve(x+1,False,True,True)+2*Solve(x+1,True,True,True)
                return Mem[(x,a,b,c)]
            else:
                Mem[(x,a,b,c)]= 2*Solve(x+1,False,True,True)
                return Mem[(x,a,b,c)]
        else:
            if(A[x]==1 and B[x]==1):
                Mem[(x,a,b,c)]= Solve(x+1,False,False,True)+Solve(x+1,False,True,True)+Solve(x+1,True,False,True)+Solve(x+1,True,True,True)
                return Mem[(x,a,b,c)]
            elif(A[x]==1):
                Mem[(x,a,b,c)]= Solve(x+1,False,False,True)+Solve(x+1,True,False,True)
                return Mem[(x,a,b,c)]
            elif(B[x]==1):
                Mem[(x,a,b,c)]= Solve(x+1,False,False,True)+Solve(x+1,False,True,True)
                return Mem[(x,a,b,c)]
            else:
                Mem[(x,a,b,c)]= Solve(x+1,False,False,True)
                return Mem[(x,a,b,c)]
    else:
        if(C[x]==1):
            if(a and b):
                Mem[(x,a,b,c)]= Solve(x+1,True,True,False)+3*Solve(x+1,True,True,True)
                return Mem[(x,a,b,c)]
            elif(a):
                if(B[x]==1):
                    Mem[(x,a,b,c)]= Solve(x+1,True,False,False)+Solve(x+1,True,False,True)+2*Solve(x+1,True,True,True)
                    return Mem[(x,a,b,c)]
                else:
                    Mem[(x,a,b,c)]= 2*Solve(x+1,True,False,True)
                    return Mem[(x,a,b,c)]
            elif(b):
                if(A[x]==1):
                    Mem[(x,a,b,c)]= Solve(x+1,False,True,False)+Solve(x+1,False,True,True)+2*Solve(x+1,True,True,True)
                    return Mem[(x,a,b,c)]
                else:
                    Mem[(x,a,b,c)]= 2*Solve(x+1,False,True,True)
                    return Mem[(x,a,b,c)]
            else:
                if(A[x]==1):
                    if(B[x]==1):
                        Mem[(x,a,b,c)]= Solve(x+1,False,False,False)+Solve(x+1,True,True,True)+Solve(x+1,True,False,True)+Solve(x+1,False,True,True)
                        return Mem[(x,a,b,c)]
                    else:
                        Mem[(x,a,b,c)]= Solve(x+1,False,False,True)+Solve(x+1,True,False,True)
                        return Mem[(x,a,b,c)]
                else:
                    if(B[x]==1):
                        Mem[(x,a,b,c)]= Solve(x+1,False,False,True)+Solve(x+1,False,True,True)
                        return Mem[(x,a,b,c)]
                    else:
                        Mem[(x,a,b,c)]= Solve(x+1,False,False,True)
                        return Mem[(x,a,b,c)]
        else:
            if(a and b):
                Mem[(x,a,b,c)]= 3*Solve(x+1,True,True,False)
                return Mem[(x,a,b,c)]
            elif(a):
                if(B[x]==1):
                    Mem[(x,a,b,c)]= Solve(x+1,True,False,False)+2*Solve(x+1,True,True,False)
                    return Mem[(x,a,b,c)]
                else:
                    Mem[(x,a,b,c)]= 2*Solve(x+1,True,False,False)
                    return Mem[(x,a,b,c)]
            elif(b):
                if(A[x]==1):
                    Mem[(x,a,b,c)]= Solve(x+1,False,True,False)+2*Solve(x+1,True,True,False)
                    return Mem[(x,a,b,c)]
                else:
                    Mem[(x,a,b,c)]= 2*Solve(x+1,False,True,False)
                    return Mem[(x,a,b,c)]
            else:
                if(A[x]==1 and B[x]==1):
                    Mem[(x,a,b,c)]= Solve(x+1,True,False,False)+Solve(x+1,False,True,False)+Solve(x+1,True,True,False)
                    return Mem[(x,a,b,c)]
                elif(A[x]==1):
                    Mem[(x,a,b,c)]= Solve(x+1,True,False,False)+Solve(x+1,False,False,False)
                    return Mem[(x,a,b,c)]
                elif(B[x]==1):
                    Mem[(x,a,b,c)]= Solve(x+1,False,True,False)+Solve(x+1,False,False,False)
                    return Mem[(x,a,b,c)]
                else:
                    Mem[(x,a,b,c)]= Solve(x+1,False,False,False)
                    return Mem[(x,a,b,c)]
        return Mem[(x,a,b,c)]



T=int(fin.readline())
Ans=""
for t in range(T):
    Ans+="Case #"+str(t+1)+": "
    A,B,C=map(int,fin.readline().split())
    A-=1
    B-=1
    C-=1
    A=list(bin(A)[2:])
    B=list(bin(B)[2:])
    C=list(bin(C)[2:])

    for i in range(len(A)):
        A[i]=int(A[i])

    for i in range(len(B)):
        B[i]=int(B[i])

    for i in range(len(C)):
        C[i]=int(C[i])

    x=max((len(A),len(B),len(C)))

    while(len(A)<x):
        A=[0]+A
    while(len(B)<x):
        B=[0]+B
    while(len(C)<x):
        C=[0]+C
    Mem={}
    Ans+=str(Solve(0,False,False,False))+"\n"
fout.write(Ans)
fout.close()
