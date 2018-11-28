#!/usr/bin/env python

import sys
import string

fairSquare=(
0,
1,
4,
9,
121,
484,
10201,
12321,
14641,
40804,
44944,
1002001,
1234321,
4008004,
100020001,
102030201,
104060401,
121242121,
123454321,
125686521,
400080004,
404090404,
10000200001,
10221412201,
12102420121,
12345654321,
40000800004,
1000002000001,
1002003002001,
1004006004001,
1020304030201,
1022325232201,
1024348434201,
1210024200121,
1212225222121,
1214428244121,
1232346432321,
1234567654321,
4000008000004,
4004009004004
)

def binary_search(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x: 
            hi = mid
        else:
            return mid
    return -1

fname=sys.argv[1]

i=open(fname,'r')
o=open(fname+'.out','w')

'''readline Split'''
def rls(i):
	out=map(int, string.split(i.readline()))
	return out[0] if len(out)==1 else out

'''Output Case#...'''
def wout(o, i, arg):
	out="Case #"+ str(i)+":"
	out+=" "+str(arg)
	#out+=" "+''.join(arg)
	#for arg in args:
	#    out+=" "+str(arg)
	out+="\n"
	o.write(out)

T=rls(i)

for x in range(T):
	a,b=rls(i)
	#print "\n", a, b
	A,B=-1,0
	for m in range(len(fairSquare)):
		if A==-1 and a<=fairSquare[m]:
			A=m#-(1 if a==fairSquare[m] else 0)
			#print "A", a, m, fairSquare[m], A

		if A!=-1 and b<=fairSquare[m]:
			B=m+(1 if b==fairSquare[m] else 0)
			#print "B", b, m, fairSquare[m], B
			break;

	#print "answer ", B, "-", A, "=", B-A
	wout(o, x+1, B-A)

