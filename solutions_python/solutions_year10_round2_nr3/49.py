import sys
from pprint import pprint

def compute_combinations(n, mod):
	res = []
	for i in xrange(n+1):
		res.append([0] * (n+1))
	res[0][0] = 1
	for i in range(1,n+1):
		res[i][0] = 1
		for j in range(1, i+1):
			res[i][j] = (res[i-1][j] + res[i-1][j-1]) % mod
	return res

def ranks(n, cmb, mod):
	'''Formula: res[n,l] = sum'''
	res = []
	for i in xrange(n+1):
		res.append([0] * (n+1))
	for i in xrange(2, n+1):
		res[i][1] = 1
	for N in xrange(3, n+1):
		for L in xrange(2, N):
			imin = max(1, 2*L - N)
			for i in range(imin, L):
				res[N][L] += res[L][i] * cmb[N-L-1][L-i-1] % mod
			res[N][L] %= mod
	return res

mod = 100003
cmb = compute_combinations(500, mod)
rank = ranks(500, cmb, mod)

with open(sys.argv[1]) as f:
	T = int(f.readline())
	for tc in xrange(1, T+1):
		n = int(f.readline().strip())
		res = 0
		for i in xrange(1, n):
			res += rank[n][i]
		res %= mod
		print "Case #{0}: {1}".format(tc, res)
