
import sys
def read():  sys.stdout.flush(); return sys.stdin.readline().strip()


def answer(c, f, x):
	rate = 2.0
	farm_time = 0.0
	results = []

	while True:
		results.append(farm_time + x / rate)
		farm_time += c / rate
		rate += f

		if len(results) >= 2 and results[-1] > results[-2]:
			break

#	print >>sys.stderr, results

	return min(results)


tests = int(read())
for test in xrange(tests):
	sc, sf, sx = read().split(" ")
	c, f, x = float(sc), float(sf), float(sx)

	print "Case #%d: %0.7f" % (test+1, answer(c, f, x))

