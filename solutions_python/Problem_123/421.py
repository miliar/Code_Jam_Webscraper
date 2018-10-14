from itertools import *
# 2**n*A-(2**n+1)>t[j]
for i in range(int(raw_input())):
    nn=[]
    A,N=map(int,raw_input().split())
    t=sorted(map(int,raw_input().split()))
    r=0
    j=0
    v=0
    nnn=0
    while j<len(t):
        if t[j]<A:
            A+=t[j]
            j+=1
        elif A==1:
            j+=1
            r+=1
        elif A+(A-1)>t[j]:
            A+=(A-1)
            A+=t[j]
            j+=1
            r+=1
        else:
            n=0
            while 2**n*A-(2**n-1)<=t[j]:
                n+=1
            # print n
            if n>len(t)-j:
                r+=len(t)-j
                j=len(t)
            else:
                nn.append((r,len(t)-j))
                A=2**n*A-(2**n-1)
                A+=t[j]
                r+=n
                v=1
                nnn+=n
                j+=1
    nn.append((r,len(t)-j))
    if v:
        r=min(a+b for a,b in nn)
    # print nn
    print"Case #"+str(i+1)+":",r
