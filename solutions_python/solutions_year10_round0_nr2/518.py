import sys

def main(fName):
	f = open(fName, "r")
	cases = int(f.readline())
	for i in xrange(cases):
		l = map(int, f.readline().split())[1:]
		m = min(l)
		nl = [x - m for x in l if x != m]
		t = lgcd(nl)
		r = t * (m / t) - m
		if r < 0:
			r += t
		print "Case #%d: %d" % (i + 1, r)
	f.close()	

def gcd(a, b):
	while b != 0:
		temp = b
		b = a % b
		a = temp
	return a

def lgcd(l):
	if len(l) == 1:
		return l[0]
	return reduce(gcd, l)

main(sys.argv[1])
