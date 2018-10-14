import scanf, sys
def liczba(): return scanf.readint(sys.stdin)
import itertools

t = liczba()
for case in xrange(1,t+1):
	A,B = liczba(), liczba()
	res = 0
	for n in xrange(A,B+1):
		s = set()
		mpow = 1
		while mpow <= n: mpow *= 10
		tenpow = 1
		for i in itertools.count(1):
			tenpow *= 10 # tenpow == 10**i
			mpow /= 10
			if not n/tenpow: break
			j = (n%tenpow)*mpow + n/tenpow
			if n < j <= B and j not in s:
				#print n, "->", j
				s.add(j)
				res += 1
	print "Case #%d:"%case, res
