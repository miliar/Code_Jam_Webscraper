#!/bin/env python3

for T in range(1,int(input())+1):
    l,k=input().split(" ")
    k=int(k)
    l=list(l)
    res=0

    for x in range(0, len(l)-k+1):
        if l[x]=="-":
            res+=1
            for y in range(x, x+k):
                if l[y]=="-":
                    l[y]="+"
                else:
                    l[y]="-"

    for x in range(len(l)-k+1, len(l)):
        if l[x]=="-":
            res="IMPOSSIBLE"

    print("Case #{}: {}".format(T, res))
