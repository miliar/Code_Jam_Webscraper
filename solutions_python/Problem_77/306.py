import sys; _tokens = sys.stdin.read().split(); _next_token = -1
def next(): global _next_token; _next_token += 1; return _tokens[_next_token]

def testcase(id):
	n = int(next())
	ans = n - sum(i+1 == int(next()) for i in xrange(n))
	print "Case #{0}: {1}.000000".format(id, ans)

ncases = int(next())
for i in xrange(ncases):
	testcase(i+1)
