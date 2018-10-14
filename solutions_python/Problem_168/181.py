import numpy as np

DOWN = 1
UP = 2
RIGHT = 3
LEFT = 4

def mark_bounds(m, i, j, dir, b, d):
	r, c = np.shape(m)

	if dir == DOWN:
		imod = 1
		jmod = 0
	elif dir == UP:
		imod = -1
		jmod = 0
	elif dir == RIGHT:
		imod = 0
		jmod = 1
	elif dir == LEFT:
		imod = 0
		jmod = -1

	while 0 <= i and i < r and 0 <= j and j < c:
		cr = m[i, j]
		if cr != '.':
			if (dir == DOWN and cr == '^') or (dir == UP and cr == 'v') or\
					(dir == LEFT and cr == '>') or (dir == RIGHT and cr == '<'):
				d[i, j] += 1
			b[i, j] += 1
			break

		i += imod
		j += jmod


def get_pegman(m):
	b = np.zeros(np.shape(m), dtype=int)
	d = np.zeros(np.shape(m), dtype=int)
	r, c = np.shape(m)

	# upper/bottom lines
	for i in xrange(c):
		mark_bounds(m, 0, i, DOWN, b, d)
		mark_bounds(m, r-1, i, UP, b, d)

	# left/right lines
	for i in xrange(r):
		mark_bounds(m, i, 0, RIGHT, b, d)
		mark_bounds(m, i, c-1, LEFT, b, d)

	if sum(sum(b == 4)) > 0:
		return "IMPOSSIBLE"

	cons = sum(sum(d > 0))
	return str(cons)


if __name__ == '__main__':
	import sys
	import time

	start_time = time.time()

	data = file(sys.argv[1], "rb").read()
	lines = data.split('\n')
	out = file(sys.argv[1] + "-sol.dat", "wb")

	idx = 1
	for i in xrange(int(lines[0])):
		r, c = lines[idx].strip().split()
		r = int(r)
		c = int(c)

		lm = []
		for l in xrange(r):
			lm.append(list(lines[idx + 1 + l].strip()))

		m = np.vstack(lm)
		out.write("Case #%d: %s\n" % (i + 1, get_pegman(m)))

		idx += r + 1

	out.close()
	print "--- %s seconds ---" % (time.time() - start_time)

