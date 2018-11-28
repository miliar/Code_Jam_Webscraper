def solve():
    t=int(input())
    for i in range(1,t+1):
        r,c=(int(j) for j in input().split())
        g=[input() for j in range(r)]
        for j in range(r):
            if any(k!='?' for k in g[j]) and not all(k!='?' for k in g[j]):
                res=''
                last=0
                for k in range(c):
                    if g[j][k]!='?':
                        res+=g[j][k]*(k-last+1)
                        last=k+1
                if len(res)!=c:
                    res+=res[-1]*(c-len(res))
                g[j]=res
        if g[0][0]=='?':
            last=r
            for k in range(r-1,-1,-1):
                if g[k][0]!='?':
                    for x in range(k+1,last):
                        g[x]=g[k]
                    last=k
            for k in range(last):
                g[k]=g[last]
        else:
            re=g[0]
            for k in range(1,r):
                if g[k][0]=='?':
                    g[k]=re
                else:
                    re=g[k]
        print("Case #{}:".format(i))
        for k in g:
            print(k)

solve()
                
                
                    
                    
