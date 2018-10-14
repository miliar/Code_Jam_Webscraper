import sys

with open(sys.argv[1]) as f:
	for x, l in enumerate(f.readlines()):
		if x == 0 or x & 1:
			continue
		n = [int(i) for i in l.split()]
		s = 0
		for i in n:
			s ^= i
		if s:
			print('Case #%i: NO' % (x // 2))
		else:
			print('Case #%i: %i' % (x // 2, sum(n) - min(*n)))

