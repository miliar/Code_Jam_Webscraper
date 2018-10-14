import math
f=math.ceil
t_case=int(input())
for t1 in range(1,t_case+1):
    n=int(input())
    ar=map(int,raw_input().split())
    ans=0
    z=max(ar)
    ans=10**9
    for i in range(1,z+1):
        t=i
        for j in ar:
            if j>i: t+=int(f((j-i)/(1.0*i)))
        #print i,t
        ans=min(ans,t)
    print 'Case #%d: %d'%(t1,ans)
        
