f = file('sample.in').read().split("\n")

cases = int(f[0])
for x in xrange(cases):
	case = f[x+1]

	l = {}
	n = 0
	for c in case:
		if not c in l:
			if n == 0: l[c] = 1
			elif n == 1: l[c] = 0
			else: l[c] = n
			n = n + 1
	base = len(l)
	if base == 1: base = 2
	num = 0
	for c in case:
		num = num * base
		num = num + l[c]
	print 'Case #'+str(x+1)+':',num
