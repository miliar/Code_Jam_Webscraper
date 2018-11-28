import sys

def doit(ins):

	s = ins[0]
	n = 0
	t = 0

	for p in xrange(0,len(s)):
		numAud = int(s[p])
		if p > t:
			inc = (p - t)
			n += inc
			t += inc

		t += numAud

	return n


if __name__ == "__main__":
	f = sys.stdin
	if len(sys.argv) >= 2:
		fn = sys.argv[1]
		if fn != '-':
			f = open(fn)

	t = int(f.readline())
	for _t in xrange(t):
		s = f.readline().split()[1:]
		n = doit(s)
		print "Case #%d: %d" % (_t+1, n)
