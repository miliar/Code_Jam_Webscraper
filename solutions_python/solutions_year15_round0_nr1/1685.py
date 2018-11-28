#!/usr/bin/env python3

def parse():
	s = input().split()[-1]
	return list(map(int,s))

def solve(l):
	k,s = 0,0
	for i,x in enumerate(l):
		if x>0:
			s += max(i-k,0)
			k += max(i-k,0)
		k += x
	return s

if __name__ == "__main__":
	t = int(input())
	for i in range(t):
		l = parse()
		s = solve(l)
		print("Case #{0}: {1}".format(i+1,s))
