import sys
import math

def topAndSide(p):
	r = p[0]
	h = p[1]
	return r*r + 2*r*h

def side(p):
	r = p[0]
	h = p[1]
	return 2*r*h	

def solve2(P,K):
	P.sort(key=lambda x: side(x), reverse=True)
	val = 0
	for k in range(K):
		val = val + side(P[k])
	return val

def solve(N,K,P):
	# r, h
	P.sort(key=lambda x: x[0], reverse=True)

	maxVal = 0
	for bChoice in range(0,N-K+1):
		val = solve2(P[bChoice+1:N],K-1) + topAndSide(P[bChoice])
		if val > maxVal:
			maxVal = val

	return maxVal * math.pi


t = int(raw_input())
for i in range(1, t + 1):
	N,K = [int(s) for s in raw_input().split(" ")]

	P = []
	for n in range(N):
		values = [int(s) for s in raw_input().split(" ")]
		P.append((float(values[0]), float(values[1])))

	result = solve(N,K,P)

	print("Case #{}: {}".format(i, result))
