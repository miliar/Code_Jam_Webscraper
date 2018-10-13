import sys

f = open(sys.argv[1])

T = f.readline()

case = 1

for l in f:
	if case <= T:
		smax, audience = l.strip().split(' ')
		standing = 0
		extra = 0
		for k in xrange(int(smax) + 1):
			short = max(0,k - standing)
			standing += int(audience[k]) + short
			extra += short
		print 'Case #%d: %d' % (case, extra)
		case += 1