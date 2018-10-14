#!/usr/bin/python
T=int(input())
for i in range(1,T+1):
    n=int(input())
    line=input().split()
    l=list( int(x) for x in line)
    y=0
    for x in l:
        y=y^x
    res="NO"
    if y==0:
        res=str(sum(l)-min(l))
    print("Case #%d: %s"%(i,res))
