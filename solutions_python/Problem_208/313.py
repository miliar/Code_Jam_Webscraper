import numpy as np

routes = []
calced = []
nn = 0

def calc_route(i, j):
	global routes
	global calced
	global nn

	if i < nn and j < nn and calced[i][j] is not None:
		return calced[i][j]

	if len(routes) == i:
		return 0

	if len(routes[i]) - 1 == j or i == j:
		calced[i][j] = routes[i][j] + calc_route(i + 1, j)
		return calced[i][j]

	calced[i][j] = min(routes[i][j] + calc_route(i + 1, j),  routes[i][i] + calc_route(i + 1, i))
	return calced[i][j]

def calc_delivery(q, n, horses, dists, pairs):
	global routes
	global calced
	global nn

	deliveries = []

	# in each cell, we have a list of length up to n. pos i in that list gives speed if horse[i] makes this city (upper cell)
	routes = []

	# deliver for 0 to n-1 city going through all (small prob)
	small_dists = [float(dists[x][x + 1]) for x in xrange(n-1)]
	for c in xrange(n-1):
		rc = []
		for hidx in xrange(c + 1):
			e, s = horses[hidx]
			if e >= sum(small_dists[hidx:c + 1]):
				tm = small_dists[c] / s
			else:
				tm = float('inf')
			rc.append(tm)

		routes.append(rc)

	calced = [[None] * n] * n
	nn = n
	deliveries.append(calc_route(0, 0))

	# return a string of floats (.7f) space separated
	return " ".join(["{0:.7f}".format(x) for x in deliveries])

if __name__ == '__main__':
	import sys
	import time

	start_time = time.time()

	data = file(sys.argv[1], "rb").read()
	lines = data.split('\n')
	out = file(sys.argv[1] + "-sol.dat", "wb")

	t = int(lines[0])
	idx = 1
	for i in xrange(t):
		[n, q] = lines[idx].split(" ")
		n = int(n)
		q = int(q)
		idx += 1

		horses = []
		for j in xrange(n):
			e, s = lines[idx + j].split(" ")
			e = int(e)
			s = int(s)
			horses.append((e, s))
		idx += n

		dists = []
		for j in xrange(n):
			dists.append([int(x) for x in lines[idx + j].split(" ")])
		idx += n

		pairs = []
		for j in xrange(q):
			u, v = lines[idx + j].split(" ")
			u = int(u)
			v = int(v)
			pairs.append((u, v))
		idx += q

		out.write("Case #%d: %s\n" % (i + 1, calc_delivery(q, n, horses, dists, pairs)))


	out.close()
	print "--- %s seconds ---" % (time.time() - start_time)
