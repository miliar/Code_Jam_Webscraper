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
	S, K = raw_input().rsplit(" ", 1)
	C, S, K = 0, [x for x in S], int(K)
	for i in range(len(S) - K + 1):
		if S[i] == '-':
			C += 1
			for j in range(K):
				S[i+j] = '+' if S[i+j] == '-' else '-' 
	if '-' in S[-K:]: print "Case #%d: IMPOSSIBLE"%(t)
	else: print "Case #%d: %d"%(t, C)
