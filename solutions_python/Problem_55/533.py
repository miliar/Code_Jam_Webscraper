#!/usr/bin/python
 
def solve():
	T = int(raw_input())
	
	for i in range(T):
		R, k, N = raw_input().split(' ')
		R = int(R)
		k = int(k)
		N = int(N)
		
		g = raw_input().split(' ')
		earnings = 0
		
		j = 0
		
		for a in range(R):
			e = 0
			for gn in range(N):
				if e+int(g[j]) <= k:
					e += int(g[j])
					j = (j + 1) % N
				else: break;
			earnings += e
	
		print "Case #" + str(i+1) + ":", earnings
		


solve()
