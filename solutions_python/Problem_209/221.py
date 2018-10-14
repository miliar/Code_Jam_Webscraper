import math

cur_rad = 0


def calc_area(p, remove_rad):
	res = 2 * math.pi * p[0] * p[1]

	if p[0] > remove_rad:
		res += math.pi * pow(p[0] - remove_rad, 2)

	return res


def sort_fun(p):
	global cur_rad

	return calc_area(p, cur_rad)


def calc_pancake_area(n, k, pans):
	global cur_rad

	# sort via height + residual radius
	cur_rad = float(0)

	cur_area = 0
	pans.sort(key=sort_fun, reverse=True)
	for x in xrange(k):
		p = pans.pop(0)
		cur_area += 2 * math.pi * p[0] * p[1]
		if cur_rad < p[0]:
			cur_rad = p[0]
			pans.sort(key=sort_fun, reverse=True)

	return cur_area + (math.pi * pow(cur_rad, 2))


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
		[n, k] = lines[idx].split(" ")
		n = int(n)
		k = int(k)
		idx += 1

		pans = []
		for x in xrange(n):
			[r, h] = lines[idx + x].split(" ")
			pans += [(int(r), int(h))]

		idx += n

		out.write("Case #%d: %.7f\n" % (i + 1, calc_pancake_area(n, k, pans)))


	out.close()
	print "--- %s seconds ---" % (time.time() - start_time)
