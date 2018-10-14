import sys

from math import *
from itertools import *
from collections import defaultdict

def lg(a) :
    sys.stderr.write(str(a)+"\n")

def sim(a) :
    s = 0
    for i,p in enumerate(a) :
	if p==0 :
	    continue
	if s>=i :
	    s += p
	else :
	    return False
    return True

def f(b) :
    for i in range(10000) :
	a = b[:]
	a[0] += i
	if sim(a) :
	    return i

t = int(sys.stdin.readline())
for testNr in range(1,t+1) :
    n,s = sys.stdin.readline().split()
    n = int(n)
    a = map(int,s)
    assert len(a)==n+1
    print "Case #%d:" % testNr , f(a)

