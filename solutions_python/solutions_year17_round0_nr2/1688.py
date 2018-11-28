#!/usr/bin/python

def func(n):
    flag=False
    for i in range(len(n)-1):
        if n[i]>n[i+1]:
            f=n[:i] 
            n=f+str(int(n[i])-1)+'9'*(len(n)-i-1)
            flag=True
            break
    if flag:
        n=func(n)
    return n




#f=open('testB','r')
#f=open('Downloads/B-small-attempt0.in','r')
f=open('Downloads/B-large.in','r')
f.readline()
C=0
for l in f:
    C+=1
    g=func(l.strip())
    print "Case #"+str(C)+":",str(int(g))







