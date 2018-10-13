import sys

f = open(sys.argv[1])

N = int(f.readline())

for i in xrange(N):
	P, K, L = map(int, f.readline().split())
	freq = map(int, f.readline().split())
	freq.sort(reverse=True)

	result = 0

	mult = 1
	count = 0

	for n in freq:
		count += 1
		if count > K:
			count = 1
			mult += 1
		result += n * mult

	print "Case #%d: %d" % (i + 1, result)
