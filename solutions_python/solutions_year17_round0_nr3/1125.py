from math import *
noTests=int(input())
for i in range(1,noTests+1):
    n,k=map(int,input().strip().split())
    if k==1:
        print("Case #{}: {} {}".format(i,ceil((n-1)/2),floor((n-1)/2)))
        continue    
    noNodes=2*n+1
    maxLevel=floor(log(noNodes,2))
    level=floor(log(k,2))
    if level==maxLevel-1:
        print("Case #{}: 0 0".format(i))
        continue

    maxNode=floor(n/(2**level))
    noMaxNode=(n-(2**level-1))%(2**level)
    b=[maxNode for _ in range(noMaxNode)]
    leftSplit=k-(2**level-1)
    if noMaxNode==0:#all nodes are maxnodes
        print("Case #{}: {} {}".format(i,ceil((maxNode-1)/2),floor((maxNode-1)/2)))
        continue   
    if leftSplit<=noMaxNode:
        print("Case #{}: {} {}".format(i,ceil((maxNode-1)/2),floor((maxNode-1)/2)))
        continue   
    else:
        print("Case #{}: {} {}".format(i,ceil((maxNode-2)/2),floor((maxNode-2)/2)))
