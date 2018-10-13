def solve2(a):
    return a[0]+a[1]//2+(a[1]&1)

def solve3(a):
    res=a[0]
    if a[1]==a[2]: return res+a[1]
    if a[1]<a[2]:
        res+=a[1]

        delta=a[2]-a[1]
        res+=delta//3

        return res+(1 if (delta % 3) else 0)

    res+=a[2]
    delta=a[1]-a[2]
    res+=delta//3

    return res+(1 if (delta % 3) else 0)

import numpy as NP
def solve4(a):
    f=NP.full((a[1]+1,a[2]+1,a[3]+1,4),-1,dtype='int')
    f[0][0][0]=0

    for i in range(a[1]+1):
        for j in range(a[2]+1):
            for k in range(a[3]+1):
                if not any((i,j,k)): continue
                for t in range(4):
                    p=[-1,f[i-1,j,k,t-1] if i else -1,f[i,j-1,k,t-2] if j else -1,f[i,j,k-1,t-3] if k else -1]
                    if p[t]>=0 : p[t]+=1

                    f[i][j][k][t]=max(p)


    return max(f[a[1]][a[2]][a[3]])+a[0]


solve={2:solve2,3:solve3,4:solve4}

T=int(input())
for i in range(T):
    N,P=map(int,input().split())
    a=[0]*P
    for data in input().split():
        a[int(data)%P]+=1

    print('Case #{}: {}'.format(i+1,solve[P](a)))

