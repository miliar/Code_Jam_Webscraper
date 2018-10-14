from decimal import *
getcontext().prec = 10
from math import pi
from itertools import combinations

def ints(l):
	return tuple([int(i) for i in l])

T = int(input())
for test in range(T):
	n, k = ints(input().split())
	dim = [0] * n
	for i in range(n):
		dim[i] = ints(input().split())
	#print(dim)
	dim = sorted(dim)[::-1]
	
	b = 0
	for p2 in combinations({i for i in range(n)}, k):
		p = sorted(p2)
		s = dim[p[0]][0] * dim[p[0]][0]
		for i in p:
			s += 2 * dim[i][0] * dim[i][1]
		if s > b:
			b = s

	print("Case #" + str(test+1) + ": " + str(pi*b) )

