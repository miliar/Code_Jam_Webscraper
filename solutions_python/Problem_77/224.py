#!/usr/bin/python

import sys

'''
fact_=[1]
for n in range(1,101):
    fact_.append(fact_[n-1]*n)
    
def fact(n):
    return fact_[n]
    
def combi(n,k):
    assert(n>k)
    return fact(n)//fact(k)//fact(n-k)

bara=[1,0,1]
for n in range(3,100):
    b=fact(n)-1
    for i in range(1,n):
        b -= combi(n,i)*bara[n-i]
    bara.append(b)

expe=[0.0,0.0,2.0]
for n in range(3,100):
    e=1
    for i in range(1,n):
        e += combi(n,i)*bara[i]*(expe[i]+1)
    e+=bara[n]
    print(e)
    e=e/(fact(n)-bara[n])
    expe.append(e)
'''

def part(tea):
    te=list(tea)
    res=[]
    for i in range(0,len(te)):
        cnt=0
        x=te[i]
        if x == -1:
            continue
        while True:
            tmp=te[x-1]
            te[x-1]=-1
            x=tmp
            cnt+=1
            if te[x-1]==-1:
                break
        res.append(cnt)
#    print("res",res)
    return res


for n,line in enumerate(open(sys.argv[1])):
    if n==0:
        continue
    if n%2==1:
        continue
    
    te=[int(x) for x in line.split()]
    
    a=0
    for p in part(te):
        if p != 1:
            a+=p
    
    print("Case #{0}: {1}.000000".format(n//2,a))


