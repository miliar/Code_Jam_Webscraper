nc = input()
for ci in range(1, nc + 1):
	a = raw_input().split()
	b, o, bt, ot = 1, 1, 0, 0
	for i in range(0, int(a[0])):
		r, n = a[1 + i * 2], int(a[2 + i * 2])
		if r == 'B':
			bt, b = max(abs(n - b) + bt, ot) + 1, n
		elif r == 'O':
			ot, o = max(abs(n - o) + ot, bt) + 1, n
	
	print "Case #{0}: {1}".format(ci, max(bt, ot))
