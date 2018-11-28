import math
input=open('chocin','r')
output=open('chocout','w')
T=int(input.readline())
for dummy in range(T):
    if dummy>0:
        output.write('\n')
    output.write('Case #'+str(dummy+1)+': ')
    [N,P]=[int(x) for x in input.readline().split()]
    G=[int(x) for x in input.readline().split()]
    D={}
    D[0]=0
    D[1]=0
    D[2]=0
    D[3]=0
    for g in G:
        x=g%P
        D[x]+=1
    M=D[0]
    if P==2:
        M=M+(D[1]+1)//2
    if P==3:
        a=min(D[1],D[2])
        b=max(D[1],D[2])
        M=M+a+(b-a+2)//3
    if P==4:
        S=[]
        for j in range(M):
            S=S+[0]
        for j in range(D[2]//2):
            S=S+[2,2]
        D[2]=D[2]%2
        a=min(D[1],D[3])
        for j in range(a):
            S=S+[1,3]
        D[1]=max(D[1],D[3])-a
        if D[2]==1 and D[1]>=2:
            S=S+[2,1,1]
            D[2]=0
            D[1]=D[1]-2
        for j in range(D[1]//4):
            S=S+[1,1,1,1]
        D[1]=D[1]%4
        for j in range(D[1]):
            S=S+[1]
        for j in range(D[2]):
            S=S+[2]
        sum=0
        M=0
        print len(S),N,P
        for x in range(N):
            if sum%4==0:
                M+=1
            sum+=S[x]
    output.write(str(M))
        
