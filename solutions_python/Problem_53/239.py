import sys

with open(sys.argv[1]) as f:
	T = int(f.readline())
	tc = 0
	for line in f:
		N, k = [int(x) for x in line.split()]
		tc += 1
		on = (k + 1) % (1 << N) == 0
		print "Case #{0}: {1}".format(tc, ("ON" if on else "OFF"))
