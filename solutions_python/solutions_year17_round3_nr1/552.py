import math
from collections import defaultdict
t=int(raw_input())
for ii in range(t):
    n,k=[int(x) for x in raw_input().split()]
    a=[]
    for i in range(n):
        rr,hh=[int(x) for x in raw_input().split()]
        a.append([rr,rr*hh])
    a.sort()
    b=[0]*(n+1)
    b[1]=a[0][1]
    j=n-1
    mx=0
    while j>=k-1:
        tmp=a[j][0]**2+2*a[j][1]
        dd=[]
        for kk in range(j):
            dd.append(a[kk][1])
        dd.sort(reverse=True)
        for kk in range(k-1):
            tmp+=(2*dd[kk])
        mx=max(mx,tmp)
        j-=1
    ans=math.pi*mx
    ans='{0:.8f}'.format(ans)
    print "Case #"+str(ii+1)+": "+str(ans)
        
