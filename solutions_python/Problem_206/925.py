from math import *
noTests=int(input())
for i in range(1,noTests+1):
    k,n=map(int,input().strip().split())
    maxm=-inf
    for j in range(n):
        d,s=map(int,input().strip().split())
        time=(k-d)/s
        if time>maxm:
            maxm=time

    result=k/maxm
    print("Case #{}: {}".format(i,result))

