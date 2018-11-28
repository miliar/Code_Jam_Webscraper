import numpy as NP

def solve():
    N,Q=map(int,input().split())

    horses=[]

    for i in range(N):
        r,s=map(int,input().split())

        horses.append((r,s))

    dis=NP.zeros((N,N))
    for i in range(N):
        dis[i]=[i if i>0 else NP.inf for i in map(int,input().split())]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                newDis=dis[i][k]+dis[k][j]
                if newDis<dis[i][j]: dis[i][j]=newDis

    tdis=NP.full((N,N),NP.inf)
    for i in range(N):
        for j in range(N):
            if dis[i][j]<=horses[i][0]:
                tdis[i][j]=dis[i][j]/horses[i][1]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                newTDis=tdis[i][k]+tdis[k][j]
                if newTDis<tdis[i][j]: tdis[i][j]=newTDis

    res=[]
    for q in range(Q):
        u,v=map(int,input().split())
        u=u-1;v=v-1

        assert not tdis[u][v] is NP.inf

        res.append(tdis[u][v])

    return ' '.join(map(str,res))

K=int(input())
for i in range(K):
    print('Case #{}: {}'.format(i+1,solve()))



