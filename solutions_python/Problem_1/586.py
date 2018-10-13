import sys

def line(): return sys.stdin.readline().rstrip('\n\r')

n = int(line())
for i in xrange(n):
	engines = {}
	s = int(line())
	for e in xrange(s):
		engines[line()] = e

	q = int(line())

	switches = 0
	# all engines mask
	allengines = (1<<s)-1
	# engines that shouldn't be used
	dontuse = 0
	for l in xrange(q):
		query = line()

		engine = engines[query]
		dontuse |= (1<<engine)
		if dontuse == allengines:
			# can't use any engine for this query.
			# must switch at this point
			switches += 1
			dontuse = 1<<engine
	
	print 'Case #%d: %d' % (i+1, switches)
