import sys

sys.setrecursionlimit(4000)

L = []

def solve(N, K):
	if (K==1):
		if N%2 == 0:
			return (N/2, N/2 -1)
		else:
			return ((N-1)/2, (N-1)/2)
	else:	
		if N%2 == 0:
			if K%2 == 0:
				return solve(N/2, K/2)
			else:
				return solve(N/2-1, (K-1)/2)
		else:
			if K%2 == 0:
				return solve((N-1)/2, K/2)
			else:
				return solve((N-1)/2, (K-1)/2)

T = int(raw_input())

for i in range(T):
	N,K = raw_input().split()
	N = int(N)
	K = int(K)
	res = solve(N, K)
	x, y = res
	print("Case #%d: %s %s"%(i+1, x, y))

