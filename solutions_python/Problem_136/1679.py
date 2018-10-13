# !/usr/bin/env python
from sys import stdin 
fout = open('outS.out','w')

def cost(c,f,x,n):
    farmCost = 0
    rate = 2.0
    if n==0:
	return x/2
    for i in xrange(int(n)):
	farmCost += c/rate
	rate += f
    return farmCost+x/rate

T = int(stdin.next().strip()) 

for i in xrange(T):
    (C,F,X)=map(float,stdin.next().strip().split())
    n=0

    while 1:
	if cost(C,F,X,n)>cost(C,F,X,n+1):
	    n += 1
	else:
	    out = cost(C,F,X,n)
	    break
    
    print>>fout,'Case #%d: %.6f' %(i+1,out)
    print 'Case #%d: %.7f' %(i+1,out)

fout.close()
