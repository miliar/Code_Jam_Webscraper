import scanf, sys
def liczba(): return scanf.readint(sys.stdin)

t = liczba()
for case in xrange(1,t+1):
	n, surps, best = liczba(), liczba(), liczba()
	res = 0
	for _ in xrange(n):
		score = liczba()
		if score >= 3*best-2:
			res += 1
		elif surps and best>=2 and score >= 3*best-4:
			res += 1
			surps -= 1
	print "Case #%d:"%case, res

