import sys
f = sys.stdin.readline

def gcd(a, b):
	while (b != 0):
		tmp = a % b
		a = b
		b = tmp
	return a

cases = int(f())
for c in xrange(cases):
	lst = map(int, f().split())
	n = lst[0]
	lst = lst[1:]
	lst.sort()
	minv = lst[0]
	t = 0
	lst = lst[1:]
	for i in lst:
		t = gcd(t, i - minv)
	if lst[0] % t == 0:
		sol = 0
	else:
		sol = t - lst[0] % t
	print 'Case #' + str(c + 1) + ': ' + str(sol)
