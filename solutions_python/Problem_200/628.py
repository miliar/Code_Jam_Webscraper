#! /usr/bin/python
from random import randint
def C(x):
	for i in range(0, len(x)-1): 
		if x[i] > x[i+1]:
			while x[i-1] == x[i]: i -= 1
			return i if i >= 0 else 0
	return len(x)
def S(N):
	N = [ ord(x) for x in N]
	j = C(N)
	if j < len(N):
		N[j:] = [N[j]-1] + [57 for x in range(len(N) - j -1)]
	return int("".join([chr(x) for x in N]))

def T(N):
	N = int("".join(N))
	while N >= 0:
		if str(N) == "".join(sorted(str(N))): return N
		N -= 1
	return 0

T = input()
for i in range(1, T+1):
	N = S(raw_input())
	print "Case #%d: %d"%(i, N)	
	
