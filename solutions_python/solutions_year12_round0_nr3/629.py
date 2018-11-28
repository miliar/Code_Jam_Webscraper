import sys

def dbg(s): sys.stderr.write(str(s))
def dbgn(s): dbg(str(s) + "\n")

def read(t): return t(raw_input())
def reads(t): return map(t, raw_input().split(" "))


def exp(n):
	c = 0
	n /= 10
	while n > 0:
		n /= 10
		c += 1
		
	return c


def shift(n, e):
	d = n % 10
	n2 = n / 10
	
	return d * e + n2


def save(c, s, n):
	if n >= A and n <= B:
		s.add(n)
		c.add(n)


T = read(int)

for t in xrange(1, T+1):
	[A, B] = reads(int)
	
	c = set([])
	
	cnt = 0
	
	for n in xrange(A, B+1):
		if n in c:
			continue
			
		#~ dbgn(n)
		
		s = set([])
		ex = exp(n)
		#~ dbgn(ex)
		e = 10 ** ex
		#~ dbgn(e)
		save(c, s, n)
		
		n2 = shift(n, e)
		sc = 1
		while n2 != n and sc <= ex:
			save(c, s, n2)	
			n2 = shift(n2, e)
			#~ dbgn(n2)
			sc += 1
			
		no = len(s)
		
		cnt += (no * (no-1)) / 2
		
		#~ dbgn(s)
	
	dbgn(len(c))
		
	print "Case #%d: %d" % (t, cnt)
