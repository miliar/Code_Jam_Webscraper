ntc = int(raw_input())
for tc in xrange(0, ntc):
	line = raw_input().split()
	n = int(line[0])
	s = int(line[1])
	p = int(line[2])
	t = [int(x) for x in line[3:]]
	
	ans = 0
	for x in t:
		if (x/3 + (x%3 > 0) >= p):
			ans += 1
		elif (x - 2 >= 0) and (p <= (x - 2)/3 + 2 <= 10) and s > 0:
			s -= 1
			ans += 1

	print 'Case #%d: %d'%(tc+1, ans)
