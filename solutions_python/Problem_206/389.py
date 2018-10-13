# horses is a list of tuples (k, s)
def calc_speed(d, n, horses):
	# keep track of max time of slowest rider
	max_tm = -1

	for i in xrange(n):
		k, s = horses[i]
		tm = float(d - k) / s

		if tm > max_tm:
			max_tm = tm

	return float(d) / max_tm


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
		[d, n] = lines[idx].split(" ")
		d = int(d)
		n = int(n)
		horses = []
		idx += 1
		for j in xrange(n):
			k, s = lines[idx + j].split(" ")
			k = int(k)
			s = int(s)
			horses.append((k, s))

		out.write("Case #%d: %.7f\n" % (i + 1, calc_speed(d, n, horses)))
		idx += n

	out.close()
	print "--- %s seconds ---" % (time.time() - start_time)
