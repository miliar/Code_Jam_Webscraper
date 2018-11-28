nc = input()
for ci in range(1, nc + 1):
	n = input()
	c = raw_input().split()
	a = []
	m, s, t = 0, 0, -1
	for x in c:
		x = int(x)
		a += [x]
		m ^= x
		s += x
		t = (x < t or t < 0) and x or t
	ans = 'NO'
	if m == 0:
		ans = s - t
	print "Case #{0}: {1}".format(ci, ans)
