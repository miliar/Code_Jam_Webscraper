import heapq
from collections import Counter
for i in range(input()):
    n,k = map(int,raw_input().strip().split())
    if n==k or (k==(n-1) and k>2):
        print "Case #{}: {} {}".format(i+1,0,0)
        continue        
    c = Counter()
    c[n]=1
    for j in range(k-1):
        temp = max(c.keys())
        c[temp]-=1
        if c[temp]==0:
            del c[temp]
        if temp%2==0:
            c[temp/2]+=1
            c[temp/2-1]+=1
        else:
            c[temp/2]+=2
    ans = max(c.keys())
    if ans%2==0:
        ans1 = ans/2
        ans2 = ans/2-1
    else:
        ans1 = ans/2
        ans2 = ans/2
    print "Case #{}: {} {}".format(i+1,ans/2,ans/2-(1-ans%2))