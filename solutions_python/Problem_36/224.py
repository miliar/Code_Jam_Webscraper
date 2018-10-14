import sys

f = sys.stdin

def cw(p, s):
	c = 0
	for i in range(len(s)):
		if s[i]==p[0]:
			if len(p) > 1:
				c += cw(p[1:], s[i+1:])
			else:
				c += 1
	return c

n = int(f.readline())
for n in range(1, n+1):
	l = f.readline()
	c = cw("welcome to code jam", l)
	print "Case #%s: %s" % (n, ("%04d" % c)[-4:])

