#!/usr/bin/python
T=int(input())
for tt in range(1,T+1):
    line=input().split()
    p=[1,1]
    t=[0,0]
    for i in range(1,len(line),2):
        x={"O":0, "B":1}[line[i]]
        y=int(line[i+1])
        ta=max( t[x]+abs(y-p[x])+1, t[1-x]+1  )
        t[x]=ta
        p[x]=y
    res=max(t)
    print("Case #%d: %d"%(tt,res))
