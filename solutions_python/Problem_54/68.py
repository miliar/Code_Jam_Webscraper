import math

def gcd(a, b):
	if (b == 0): return a
	return gcd(b, a%b)
def gcdv(v):
	res = v[0]
	for e in v:
		res = gcd(res, e)
	return res

T = int(raw_input())
for tc in range(1, T+1):
	IN = raw_input().split(' ')
	N = int(IN[0])
	t = [0]*N;
	d = [0]*(N-1)
	for k in range(0, N): t[k] = int(IN[k+1])
	for k in range(1, N): d[k-1] = abs(t[k] - t[k-1])
	g = gcdv(d)
	m = t[0] / g
	if g*m < t[0]: m += 1
	print 'Case #%d: %d ' % (tc, (g*m - t[0]))

