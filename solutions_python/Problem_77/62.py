import sys

with open(sys.argv[1]) as f:
	for x, l in enumerate(f.readlines()):
		if x == 0 or x & 1:
			continue
		n = [int(i) for i in l.split()]
		s = [0] * len(n)
		pos = 0
		t = 1
		exp = 0

		while True:
			current = 0
			while True:
				if s[pos] != 0:
					break
				s[pos] = t
				pos = n[pos] - 1
				t += 1
				current += 1
			exp += 0 if current == 1 else current

			pos = 0
			while pos < len(n):
				if s[pos] == 0:
					break
				pos += 1
			else:
				break

		print('Case #%i: %.6f' % (x // 2, exp))
