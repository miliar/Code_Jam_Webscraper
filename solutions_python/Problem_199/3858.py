k=int(input())

ans=[]

while (k>0):
    count=0
    I=input()
    Q1=I.split(" ")[0]
    Q2=int(I.split(" ")[1])
    S=list(Q1)
    N=len(S)
    R=["+"]*N

    for i in range(N-Q2):
        if S[i]=='-':
            count+=1
            for j in range(i,i+Q2):
                if S[j]=='-':
                    S[j]='+'
                else:
                    S[j]='-'
    
    for i in range(N-Q2+1,N):
        if S[i]=='-':
            count+=1
            for j in range(N-Q2,N):
                if S[j]=='-':
                    S[j]='+'
                else:
                    S[j]='-'

    if S==R:
        ans.append(count)
    else:
        ans.append("IMPOSSIBLE")
    
    k-=1

for i in range(len(ans)):
    print("Case #"+str(i+1)+": "+str(ans[i]))
    
