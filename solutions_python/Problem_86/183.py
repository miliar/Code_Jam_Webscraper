import sys, itertools

filename = sys.argv[1]
f = open(filename)
o = open(filename + ".out", "wt")
num_tests = int(f.readline())
for t in range(1, num_tests+1):
	n, l, h = [int(x) for x in f.readline().split()]
	cs = [int(x) for x in f.readline().split()]
	freq = -1
	for i in range(l, h+1):
		if all([i % c == 0 or c % i == 0 for c in cs]):
			freq = i
			break
	res = "NO" if freq == -1 else str(freq)
	o.write("Case #%d: %s\n" % (t, res))
o.close()

