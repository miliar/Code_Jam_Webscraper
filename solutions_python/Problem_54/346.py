from fractions import gcd
from math import *
f=open("B.in",'r')
g=open("B.out",'w')
t=int(f.readline())
for ind in range(t):
    a=[long(x) for x in f.readline().split()][1:]
    print a
    gc=abs(a[0]-a[1])
    for i in range(len(a)):
        for j in range(i,len(a)):
            gc=gcd(gc,abs(a[i]-a[j]))
            if gc==1: break
        if gc==1: break
    ans=gc-(a[0]%gc)
    if ans==gc: ans=0
    print ans
    g.write("Case #"+str(ind+1)+": "+str(ans)+"\n")