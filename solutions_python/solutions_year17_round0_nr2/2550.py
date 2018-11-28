#!/bin/env python3

def run():
    n=list(input())
    res=[]
    if len(n)<=1:
        return n

    i=0
    while i<len(n)-1 and n[i]<=n[i+1]:
        i+=1

    if i==len(n)-1:
        return n

    for x in range(i+1, len(n)):
        n[x]="9"

    if i==0:
        n[i]=str(int(n[i])-1)
        if n[i]=="0":
            n=n[1:]


    while i>0:
        if n[i]>n[i-1]:
            n[i]=str(int(n[i])-1)
            break
        else:
            n[i]="9"
            if i==1:
                n[0]=str(int(n[0])-1)
                if n[0]=="0":
                    n=n[1:]
                break
            i-=1
        

    return n

for T in range(1,int(input())+1):
    print("Case #{}: {}".format(T, "".join(run())))
