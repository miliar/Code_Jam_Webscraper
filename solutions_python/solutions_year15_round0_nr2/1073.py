import sys
import math
import copy

def solve(P):
	x = max(P)
	res = x
	if x <= 3:
		return x 

	ix = P.index(x)
	for d in [2,3]:
		if x < 9 and d == 3:
			continue
		P[ix] = x / d
		P.append(x - x / d)
		res = min(res, solve(P) + 1)
		P[ix] = x
		del P[-1]

	return res

T = int(raw_input())

for tc in range(T):
	D = int(raw_input())
	r = raw_input()
	P = r.split()
	for i in range(D):
		P[i] = int(P[i])
	print "Case #{:d}: {:d}".format(tc+1, solve(P))