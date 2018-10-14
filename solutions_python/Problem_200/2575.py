# num is a string
def print_last_tidy(num):
	ln = [int(x) for x in num]
	n = len(ln)

	bad_idx = -1
	for i in xrange(n - 2, -1, -1):
		if ln[i] > ln[i + 1]:
			bad_idx = i
			ln[i] -= 1

	if bad_idx == -1:
		return num

	new_num = "".join([str(x) for x in ln[: bad_idx + 1]]) + "9" * (n - bad_idx - 1)

	# get rid of leading zeros
	new_num = new_num.lstrip("0")

	return new_num

if __name__ == '__main__':
	import sys
	import time

	start_time = time.time()

	data = file(sys.argv[1], "rb").read()
	lines = data.split('\n')
	out = file(sys.argv[1] + "-sol.dat", "wb")

	t = int(lines[0])
	for i in xrange(t):
		num = lines[i + 1]
		out.write("Case #%d: %s\n" % (i + 1, print_last_tidy(num)))

	out.close()
	print "--- %s seconds ---" % (time.time() - start_time)
