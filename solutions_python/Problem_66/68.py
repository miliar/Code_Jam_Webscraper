import sys

from math import *
from itertools import *
from collections import defaultdict

def lg(a) :
    sys.stderr.write(str(a)+"\n")

def sol2(heap,m,p) :
    ins = set()
    for i,v in enumerate(m) :
	hp = len(m)/2 + i/2
#	print "i,hp",i,hp
	l = 0
	while hp>=1 :
#	    print "hp,l,v",hp,l,v
	    if v<=0 :
		ins.add(hp)
	    l += 1
	    hp /= 2
	    v -= 1
#	print l,p
	assert l==p
#	assert False
#    print ins
    return len(ins)*heap[1]

def sol(heap,head,level,p,m) :
    x = 2*head
    y = 2*head+1
    if x>=len(m) :
	return 
    c = m[head]

t = int(sys.stdin.readline())
for testNr in range(1,t+1) :
    p = int(sys.stdin.readline())
    m = map(int,sys.stdin.readline().split())
    assert len(m)==2**p
    heap = []
    for i in range(p) :
	x = map(int,sys.stdin.readline().split())
	assert len(x)==2**(p-i-1)
	heap = x + heap	
    heap = [ -1e12 ] + heap
#    print heap
#    print m
    s = sol2(heap,m,p)
#    s = sol(heap,1,0,p,m)
    print "Case #%d:" % testNr ,
    print s

