#!/usr/bin/env python3

def parse():
	x,r,c = map(int,input().split())
	return x,r,c

def solve(x,r,c):
	n,m = min(r,c),max(r,c)
	if x==1: return 0
	if x==2: return n*m%2
	if x==3:
		if n==1 or m<3: return 1
		return n*m%3>0
	return not (n>2 and m==4)

if __name__ == "__main__":
	t = int(input())
	for i in range(t):
		x,r,c = parse()
		s = solve(x,r,c)
		print("Case #{0}: {1}".format(i+1,("GABRIEL","RICHARD")[s]))
