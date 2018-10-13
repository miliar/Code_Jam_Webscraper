import sys

from math import *
from itertools import *
from collections import defaultdict

def lg(a) :
    sys.stderr.write(str(a)+"\n")


QT = { "ij":"k", "ik":"-j", "jk":"i", "ji":"-k", "ki":"j", "kj":"-i" }

def nmul(isNeg, q) :
    if not isNeg :
	return q
    if q.startswith("-") :
	return q[-1]
    else :
	return "-"+q

def elements() :
    b = list("1ijk")
    b += [ "-"+p for p in b]
    return b

def qmul(pc,qc) :
    p,q = pc,qc
    sgn = (p[0]=="-") != (q[0]=="-")
    p = p[-1]
    q = q[-1]
    if p=="1" :
	return nmul(sgn,q)
    if q=="1" :
	return nmul(sgn,p)
    if p==q :
	return nmul(sgn,"-1")
    return nmul(sgn,QT[p+q])

def test() :
    for p in elements() :
	for q in elements() :
	    print qmul(p,q),
	print

def qmulmul(a) :
    return reduce( lambda p,q : qmul(p,q), a, "1" )

def qsqr(p) :
    return qmul(p,p)

def qpow(p,n) :
    cur = p
    tot = "1"
    while n>0 :
	if n%2 :
	    tot = qmul(tot,cur)
	n /= 2
	cur = qsqr(cur)
    return tot

def f(a,x) :
    if False :
	for p in a :
	    cur = qmul(cur,p)
	    print cur,
	print
	mm = qmulmul(a)
	print mm
	print qpow( mm, x )

    if qpow( qmulmul(a), x ) != "-1" :
	return "NO"
    lim = min((x,8))
    cur = "1"
    foundI = False
    for i,p in enumerate(a*lim) :
	if i%(len(a)*4)==0 :
	    assert cur=="1"
	if i%(len(a)*2)==0 :
	    assert cur in ("1","-1")
	cur = qmul(cur,p)
	if cur=="i" :
	    foundI = True
	# print cur,foundI,
	if cur=="k" and foundI :
	    return "YES"
    return "NO"


t = int(sys.stdin.readline())
for testNr in range(1,t+1) :
    l,x = map(int,sys.stdin.readline().split())
    a = tuple(sys.stdin.readline().strip())
    c = f(a,x)
    print "Case #%d:" % testNr , c
