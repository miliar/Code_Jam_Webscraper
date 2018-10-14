import sys
from fractions import gcd

data = [x.strip() for x in sys.stdin.readlines()]

C = int(data.pop(0))
testcases = []
for line in data:
	elems = line.split(' ')
	N = int(elems.pop(0))
	testcases.append([long(x) for x in elems])

for i, events in enumerate(testcases):
	diffs = []
	for j in xrange(len(events) - 1):
		diffs.append(abs(events[j] - events[j + 1]))
	diffs.append(abs(events[-1] - events[0]))

	m = gcd(diffs[0], diffs[1])
	for j in xrange(2, len(diffs)):
		m = gcd(m, diffs[j])

	r = events[0] % m

	y = (m - r) if r != 0 else 0

	print "Case #" + str(i + 1) + ": " + str(y)

