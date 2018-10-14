def blackRings(r, t):
	rings = 0
	while t > 0:
		p = (r+1)**2 - r**2
		t = t-p
		r += 2
		if t >= 0:
			rings += 1

	return rings

INPUT_FILE = "paint.in"
with open(INPUT_FILE, 'r') as fin:
	T = int(fin.readline().rstrip())

	with open('paint.out', 'w') as fout:
		for i in range(0, T):
			r, t = map(int, fin.readline().rstrip().split(' '))
			rings = blackRings(r, t)
			fout.write("Case #%s: %s\n" % (str(i+1), str(rings)))

