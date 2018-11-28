import sys

with open(sys.argv[1]) as f:
	x = 0
	for line in f:
		x += 1
		if x == 1:
			continue
		btns = line.split()
		i = 1
		o, b = 1, 1
		ot, bt = 0, 0
		t = 0
		while i < len(btns)-1:
			dest = int(btns[i+1])
			if btns[i] == 'O':
				t += max(0, abs(dest - o) - (t - ot)) + 1
				o = dest
				ot = t
			else:
				t += max(0, abs(dest - b) - (t - bt)) + 1
				b = dest
				bt = t
			i += 2

		print('Case #%i: %i' % (x-1, t))
