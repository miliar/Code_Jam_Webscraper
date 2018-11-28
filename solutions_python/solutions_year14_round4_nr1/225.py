#!env python3

from codejam import *

@codejam
def solve():
	N, X = [int(s) for s in stdin.readline().split()]
	S = [int(s) for s in stdin.readline().split()]
	S.sort()
	total = 0
	while len(S) > 0:
		a = S.pop()
		b = S[0] if len(S) > 0 else 0
		if a+b <= X and len(S)>0:
			S.pop(0)
		#print (a,b)
		total = total + 1
	#print (N, X, S)
	return total

	

