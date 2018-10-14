import sys

def estimate(A, a):
	if A > a:
		return 0, A + a
	else:
		k = 1
		p = 2
		while True:
			B = p * A - (p - 1)
			if B > a:
				return k, B + a
			k += 1
			p *= 2

def have_to_skip(A, a):
	N = len(a)
	i = 0
	while i < N:
		if A <= a[i]:
			break
		i += 1
	return N - i

def solve(A, a):
	if A == 1:
		return len(a) # skip all
	if len(a) == 0:
		return 0
	m, B = estimate(A, a[0])
	m += solve(B, a[1:])
	sk = have_to_skip(A, a)
	return min(m, sk)

T = int(sys.stdin.readline())
for _ in range(T):
	A, N = map(int, sys.stdin.readline().split())
	a = map(int, sys.stdin.readline().split())
	a.sort()
	answer = solve(A, a)
	print 'Case #%d:' % (_ + 1), answer