import sys; _tokens = sys.stdin.read().split(); _next_token = -1
def next(): global _next_token; _next_token += 1; return _tokens[_next_token]

def testcase(id):
	n = int(next())
	cur_o = cur_b = 1
	wasted_o = wasted_b = 0
	time = 0
	for i in xrange(n):
		clr = next()
		npos = int(next())
		if clr == 'O':
			togo = abs(cur_o - npos)
			addtime = max(0, togo - wasted_o) + 1
			cur_o = npos
			time += addtime
			wasted_b += addtime
			wasted_o = 0
		else:
			togo = abs(cur_b - npos)
			addtime = max(0, togo - wasted_b) + 1
			cur_b = npos
			time += addtime
			wasted_o += addtime
			wasted_b = 0
	print "Case #{0}: {1}".format(id, time)

ncases = int(next())
for i in xrange(ncases):
	testcase(i+1)
