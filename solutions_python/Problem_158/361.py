def solve():
	x,n,m = map(int, raw_input().split())
	if n > m:
		n, m = m, n
	if x == 1:
		return True
	if x == 2:
		if (n * m) % 2 == 1:
			return False
		return True
	if x == 3:
		if (n * m) % 3 > 0:
			return False
		if n == 1:
			return False
		return True
	if x == 4:
		if (n * m) % 4 > 0:
			return False
		if m == 2:
			return False
		if n < 3:
			return False
		return True

t = int(raw_input())

man = ['GABRIEL','RICHARD']

for tt in xrange(t):
	print 'Case #{}: {}'.format(tt + 1, man[1 - solve()])