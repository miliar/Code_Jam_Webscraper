
def shift(x):
	return x[-1]+x[:-1]
	

t = input()


for i in xrange(t):
	a,b = map(int, raw_input().split())

	pair = 0
	for x in xrange(a,b+1):
		s = str(x)
		m = {}
		for j in xrange(len(s)-1):
			s = shift(s)
			tmp = int(s)
			if s[0] != "0" and tmp > x and tmp <= b:
				if s not in m:
					m[s] = 1
					pair = pair + 1

	print "Case #%d: %d" % (i+1, pair)


