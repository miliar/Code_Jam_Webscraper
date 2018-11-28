import sys; _tokens = sys.stdin.read().split(); _next_token = -1
def next(): global _next_token; _next_token += 1; return _tokens[_next_token]

def testcase(id):
	print "Case #{0}:".format(id)
	n = int(next())
	won = [next() for i in xrange(n)]
	opp = [sum(1 for j in i if j != '.') for i in won]
	wp = []
	for i in xrange(n):
		wp.append(1.0 * sum(int(x) for x in won[i] if x != '.') / opp[i])
	owp = []
	for i in xrange(n):
		twp = 0
		nop = 0
		for j in xrange(n):
			if won[i][j] == '.':
				continue
			nop += 1
			a = sum(int(x) for k, x in enumerate(won[j]) if x != '.' and k != i)
			b = opp[j] - 1
			twp += a * 1.0 / b
		owp.append(1.0 * twp / nop)
	oowp = []
	for i in xrange(n):
		oowp.append(sum(owp[j] for j, x in enumerate(won[i]) if x != '.') / opp[i])
	for i in xrange(n):
		print "{0:.7}".format(0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i])

ncases = int(next())
for i in xrange(ncases):
	testcase(i+1)
