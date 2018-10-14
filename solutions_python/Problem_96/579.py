T = int(raw_input())

for case_num in xrange(1, T+1):
	case = [int(x) for x in raw_input().split()]
	(N, S, p), t = case[:3], case[3:]

	definite = possible = 0
	for score in t:
		if score >= 3*p-2:
			definite += 1
		elif score >= 3*p-4 and score >= p:
			possible += 1
	best = definite + min(possible, S)
	print "Case #%d: %d" % (case_num, best)