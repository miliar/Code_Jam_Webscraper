#!/usr/bin/env python3

import sys
sys.stdin=open('A-large.in')
sys.stdout=open('A.out','w')
for kase in range(int(input())):
    s=input().split()
    le=int(s[0])
    del s[0]
    l=[]
    for i in range(le):
        l.append(s[0:2])
        del s[0:2]
    a,b,ans=1,1,0
    while l:
        na,nb=a,b
        for i in l:
            if i[0]=='O':
                na=int(i[1])
                break;
        for i in l:
            if i[0]=='B':
                nb=int(i[1])
                break
        if l[0][0]=='O':
            cst=abs(na-a)+1
            ans+=cst
            if abs(nb-b)<=cst:
                b=nb;
            else:
                b+=(1 if nb>b else -1)*cst
            a=na
        else:
            cst=abs(nb-b)+1
            ans+=cst
            if abs(na-a)<=cst:
                a=na;
            else:
                a+=(1 if na>a else -1)*cst
            b=nb
        del l[0]
    print("Case #{0}: {1}".format(kase+1, ans))
