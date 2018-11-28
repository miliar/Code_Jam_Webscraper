T = int(raw_input())

for case in range(1,1+T):
	N,PD,PG = tuple(map(int, raw_input().split()))
	broken = (PG == 0 and PD != 0) or (PG == 100 and PD != 100)
	if not broken:	
		numerator, denominator = PD,100
		for d in [2,2,5,5]:
			if (numerator % d) == 0:
				numerator /= d
				denominator /= d
		broken = denominator > N
	answer = "Broken" if broken else "Possible"
	print "Case #%d: %s" % (case, answer)
