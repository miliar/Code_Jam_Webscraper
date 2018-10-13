#Google CodeJam Qualification Round Problem 3 by :
#*******************_ LBSREX _*******************
import math
t=int(raw_input())
for i in xrange(t):
    n,k=map(int,raw_input().split())
    lis=list([1,n,1])
    for j in range(k-1):
        x=lis.index(max(lis))
        lis[x:x+1]=int(math.floor(float(lis[x]-1)/2)),1,int(math.ceil(float(lis[x]-1)/2))
    mx=math.ceil(float(max(lis)-1)/2)
    mn=math.floor(float(max(lis)-1)/2)
    print "Case #"+str(i+1)+": "+str(int(mx))+" "+str(int(mn))
