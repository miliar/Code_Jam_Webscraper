#!/usr/bin/python3

def f(n):
	return n * (2*r+1) + 2*n*(n-1);

def bs(lo,hi):
	if(hi-lo <= 3):
		for n in range(lo-1, hi+1):
			if(f(n) > t):
				return n-1
		return -1
	mid = (hi+lo)//2
	g = f(mid)
	if(g == t):
		return mid
	elif(g > t):
		return bs(lo,mid)
	return bs(mid,hi)

cases = int(input())
for q in range(1,cases+1):
	line = input().split()
	r = int(line[0])
	t = int(line[1])
	print("Case #%d: %d"%(q, bs(0, 1000000000) ))
