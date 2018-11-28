# ls - list of True and False
def flip_one(ls, idx, k):
	for i in xrange(idx, idx + k):
		ls[i] = not ls[i]

def print_flips(s, k):
	n = len(s)
	ls = [True if x == '+' else False for x in list(s)]

	if k > n:
		return "IMPOSSIBLE"

	i = 0
	flips = 0
	while i < n - k + 1:
		if not ls[i]:
			flip_one(ls, i, k)
			flips += 1
		i += 1

	if False in ls:
		return "IMPOSSIBLE"

	return str(flips)

if __name__ == '__main__':
	import sys
	import time

	start_time = time.time()

	data = file(sys.argv[1], "rb").read()
	lines = data.split('\n')
	out = file(sys.argv[1] + "-sol.dat", "wb")

	t = int(lines[0])
	for i in xrange(t):
		[s, k] = lines[i + 1].split(" ")
		k = int(k)

		out.write("Case #%d: %s\n" % (i + 1, print_flips(s, k)))

	out.close()
	print "--- %s seconds ---" % (time.time() - start_time)