
def gcd(a, b):
	if a % b == 0:
		return b
	else:
		return gcd(b, a%b)

ecase = input()
for ecount in range(1, ecase + 1):
	s = raw_input()
	sa = s.split()
	sna = []
	for x in sa:
		sna.append(int(x))
	n = sna[0]
	sna.remove(n)
	g = 0

	for i in range(0, n - 1):
		if sna[i] != sna[i+1]:
			if g == 0:
				g = abs(sna[i] - sna[i+1])
			else:
				g = gcd(g, abs(sna[i] - sna[i+1]))
	a = g - sna[0] % g
	if a == g:
		a = 0
	print "Case #%d: %d" % (ecount, a)

