from math import *

def palin(n):
    n=str(n)
    for i in range(len(n)/2):
        if n[i-1]!=n[-i]:
            return False
    return True

l=[x**2 for x in range(1,32) if (palin(x) and palin(x**2))]

T=int(raw_input())
for i in range(T):
    A,B=raw_input().split(" ")
    A,B=int(A),int(B)
    ll=[x for x in l if (x>=A and x<=B)]
    s="Case #"+str(i+1)+": "+str(len(ll))
    print s
