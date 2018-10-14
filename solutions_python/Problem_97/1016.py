#!/usr/bin/python
def work(num):
    tmps=str(num)
    ret=0
    for i in range(1,len(tmps)):
        tmp=tmps[i:]+tmps[:i]
        if ((int(tmp)>int(tmps)) and (int(tmp)<=b)):
            ret = ret+1
    return ret
T=input()
for Te in range(1,T+1):
    a,b=raw_input().split()
    a=int(a)
    b=int(b)
    ans=0
    for i in range(a,b+1):
        ans= ans + work(i)
    print("Case #%d: %d"%(Te,ans))

