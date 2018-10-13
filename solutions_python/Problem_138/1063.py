T = input()

for case in range(1, T + 1):
	N = input()
	a = map(float, raw_input().split())
	b = map(float, raw_input().split())
	a.sort()
	b.sort()
	b = b[::-1]
	a = a[::-1]
	# print a, b

	c = a[:]
	d = b[:]
	badwin = 0
	# Regular
	while len(c) > 0:
		n = c[-1]
		c = c[:-1]
		if n > d[0]:
			badwin += 1
			d = d[:-1]
		elif n < d[-1]:
			d = d[:-1]
		else:
			i = -1
			while d[i] < n:
				i -= 1
			d = d[:i] + d[i + 1:]


	# Deceitful
	win = 0
	while len(a) > 0:
		# kill any blocks which N cannot beat
		while len(a) > 0 and b[0] > a[0]:
			b = b[1:]
			a = a[:-1]
		while len(a) > 0 and b[-1] > a[-1]:
			b = b[1:]
			a = a[:-1]
		# print a, b
		while len(a) > 0 and a[-1] > b[-1]:
			a = a[:-1]
			b = b[:-1]
			win += 1

	print "Case #%d:" % case, win, badwin