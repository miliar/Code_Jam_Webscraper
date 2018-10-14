out=open("out.txt","w")
with open("A-large.in") as file:
    T=int(file.readline())
    #print T
    for case in range(T):
        s,K=file.readline().split()
        N=len(s)
        K=int(K)
        a=[0]*N
        for i in range(N):
            if s[i]=='+':
                a[i]=1
        #print a,K
        res=0
        for i in range(N-K):
            if a[i]==0:
                for j in range(i,i+K):
                    a[j]= not a[j]
                res+=1
        sm=sum(a[N-K:])
        if sm==0:
            ans=str(res+1)
        elif sm==K:
            ans=str(res)
        else:
            ans="IMPOSSIBLE"
        out.write("Case #"+str(case+1)+": "+ans+"\n")
out.close()

