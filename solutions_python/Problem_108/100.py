import sys
from collections import defaultdict

input = sys.stdin
output = sys.stdout

def go(c, l, k = 0):
#	print ' ' * k, c, l
	if D <= c + l:
		return True
	passed[c] = l
	for v in V:
		if abs(v[0] - c) <= l:
			c2 = v[0]
			l2 = min(v[1], abs(v[0] - c))
			if passed[c2] >= l2:
				continue
			if go(c2, l2, k + 1):
				return True
	else:
		return False

T = int(input.readline())
for t in range(T):
	N = int(input.readline())
	V = []
	for i in range(N):
		V.append([int(j) for j in input.readline().split(' ')])
	D = int(input.readline())
	p = V[0]
	passed = defaultdict(int)
	passed[p[0]] = p[1]
	result = 'YES' if go(p[0], min(p[0], p[1])) else 'NO'
	print 'Case #{t}: {result}'.format(t = t + 1, result = result)
