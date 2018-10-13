#!/usr/bin/env pypy3



def sol(a,n):
	x,e=max(a),1
	while e<x:
		y=0
		for t in a:
			y+=(t-1)//e
		x=min(x,e+y)
		e+=1
	return x 

	
for i in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	print("Case #%d: %d"%(i+1,sol(a,n)))
	
