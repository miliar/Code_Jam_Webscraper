class streamreader:
	def __init__(_, s): _.t = (t for t in s.read().split())
	def __div__(_, t): return (t)(_.t.next())

def jam(parser, solver):
	import sys
	reader = streamreader(sys.stdin)
	for i, answer in enumerate( [ apply(solver, inp) for inp in [parser(reader) for i in xrange(reader/int)] ] ):
		print 'Case #%d:' % (i + 1), answer	