#! /usr/bin/python

IMPOSSIBLE = "Impossible"
debug = False

def field(data, rotate=False):
	if rotate:
		d = [['.' for i in xrange(len(data))] for j in xrange(len(data[0]))]
		for i in xrange(len(data)):
			for j in xrange(len(data[0])):
				d[j][i] = data[i][j]
		data = d
	return '\n'.join([''.join(i for i in row) for row in data])

def solve(input_data):
	r, c, m = input_data
	
	# r <= c
	rotate = False
	if c < r:
		r, c = c, r
		rotate = True

	if r == 1:
		res = [['*' for i in xrange(m)] + ['.' for i in xrange(c - m - 1)] + ['c']]
		return field(res, rotate)

	if r == 2 and c == 2 and m == 0:
		return "c.\n.."

	if r == 2 and c == 2 and m != 0 and m != 3:
		return IMPOSSIBLE

	if r == 2 and c == 2 and m == 3:
		return 'c*\n**'

	if r == 2 and m == c*r - 1:
		data = [ ['c'] + ['*' for i in xrange(c - 1)],
				 ['*' for i in xrange(c)] ]
		return field(data, rotate)

	if r == 2 and m % 2 == 1:
		return IMPOSSIBLE

	data = [['.' for i in xrange(c)] for j in xrange(r)]
	data[0][0] = 'c'

	lc = c - 1
	while m >= r and lc >= r:
		for i in xrange(r):
			data[i][lc] = '*'
		m -= r
		lc -= 1

	shift = lc - r + 1

	if shift != 0: # m < r
		while m > 0:
			data[r - 1][lc] = '*'
			lc -= 1
			m -= 1

		return field(data, rotate)


	l = r

	while True:
		if debug: print 'l = ', l, ' m = ', m, ' shift = ', shift
		if l == 3 and (m == 2 or m == 4):
			return IMPOSSIBLE
		if l == 2 and m != 0 and m != 3:
			return IMPOSSIBLE

		if l == 2 and m == 3:
			data[0][1] = '*'
			data[1][0] = '*'
			data[1][1] = '*'
			m = 0
			break

		if m >= 2*l - 1:
			if debug: print 1
			for i in xrange(l):
				data[i][shift + l - 1] = '*'
				data[l - 1][shift + i] = '*'
			m = m - 2*l + 1
			l = l - 1
			continue

		elif m == 2*l - 2:
			if debug: print 2
			for i in xrange(l):
				data[i][shift + l - 1] = '*'
			for i in xrange(l - 2):
				data[i + 2][shift + l - 2] = '*'
			break

		elif l <= m: # <= 2*l - 3
			if debug: print 3
			for i in xrange(l):
				data[i][shift + l - 1] = '*'
			for i in xrange(m - l):
				data[l - 1][shift + l - 2 - i] = '*'
			break

		elif m == l - 1:
			if debug: print 4
			for i in xrange(m - 1):
				data[l - 1 - i][shift + l - 1] = '*'
			data[l - 1][shift + l - 2] = '*'
			break

		else:
			if debug: print 5
			for i in xrange(m):
				data[l - 1 - i][shift + l - 1] = '*'
			break


	return field(data, rotate)

def read_input():
	return map(int, raw_input().split())

def main():
	T = int(raw_input())
	for t in xrange(T):
		print "Case #%d:\n%s" % (t + 1, solve(read_input()))

if __name__ == "__main__":
	main()