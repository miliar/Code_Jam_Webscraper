#! /usr/bin/python

M = {}
def A(n): n1 = n / 2; return n1, n1-1 if n % 2 == 0 else n1
def B(K):
	mk = M.keys()
	m = max(mk)
	n = M[m]
	if n >= K: return m
	else:
		del M[m]
		a, b = A(m)
		if a not in mk: M[a] = 0
		if b not in mk: M[b] = 0
		M[a] += n
		M[b] += n
		return B(K-n)


T = input()
for t in xrange(1, T+1):
	N, K = [int(x) for x in raw_input().split()]
	M = {N:1}
	print "Case #%d: "%(t) + "%d %d"%A(B(K))
	
