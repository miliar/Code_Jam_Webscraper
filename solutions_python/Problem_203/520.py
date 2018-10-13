import sys
import numpy as np

def uni(X):
	u = set()
	for c in X:
		for x in c:
			if (x not in u) and (x != '?'):
				u.add(x)
	return u

def solve(X):
	R = len(X)
	if R == 0:
		return []
	if len(uni(X)) == 1:
		x = list(uni(X))[0]
		for i in xrange(R):
			X[i] = list(x*len(X[i]))
		return X
	for i in xrange(1,R):
		if len(uni(X[:i])) > 0 and len(uni(X[i:])) > 0:
			return solve(X[0:i]) + solve(X[i:])
	X = np.array(X)
	C = X.shape[1]
	for j in xrange(1,C):
		X1, X2 = X[:,:j].tolist(), X[:,j:].tolist()
		#print X1, X2
		if len(uni(X1)) > 0 and len(uni(X2)) > 0:
			X1 = solve(X1)
			X2 = solve(X2)
			#print X1, X2
			X1, X2 = np.array(X1), np.array(X2)
			#print X1.shape, X2.shape
			ret = np.concatenate((X1, X2), axis=1)
			#print ret.shape, X.shape
			assert(ret.shape == X.shape)
			return ret.tolist()
	assert(False)

T = int(sys.stdin.readline())

for t in xrange(T):
	R, C = map(int, sys.stdin.readline().split())
	X = []
	for r in xrange(R):
		c = list(sys.stdin.readline().strip())
		assert(len(c) == C)
		X.append(c)
	print('Case #%d:' % (t+1))
	ans = solve(X)
	for l in ans:
		print(''.join(l))
