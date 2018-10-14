#!/usr/bin/pypy
import sys
if sys.version_info[0]<=2:
	range=xrange
	input=raw_input
from random import randrange

ops0=0
ops1=0
def solve0(n):
	global ops0
	for i in range(n,-1,-1):
		ops0+=1
		l=10
		k=i
		while k:
			x=k%10
			k//=10
			if x>l:
				break
			l=x
		else:
			return i
	return 0

def solve1(n):
	m,d=n,1
	l=10
	while d<=m:
		x=(m//d)%10
		if x>l or m>n:
			m=m-(m%d)-1
			l=9
		else:
			l=x
			d*=10
	return m

cases=int(input().strip())
for cs in range(1,cases+1):
	n=int(input().strip())
	print("Case #"+str(cs)+": "+str(solve1(n)))
