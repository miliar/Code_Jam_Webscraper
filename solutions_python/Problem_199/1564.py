#!/usr/bin/python

#f=open('test','r')
#f=open('Downloads/A-small-attempt0.in','r')
f=open('Downloads/A-large.in','r')
f.readline()
C=0
for l in f:
    C+=1
    p, k = l.split(' ')
    n = len(p)
    p = [0 if x=='-' else 1 for x in p]
    k=int(k)
    r = 0
    while sum(p)!=n:
        z = p.index(0)
        if z+k>n:
            break
        for i in range(k):
            p[z+i] ^= 1
        r+=1
        
    if sum(p)!=n:
        print "Case #"+str(C)+": IMPOSSIBLE"
    else:
        print  "Case #"+str(C)+":",r







