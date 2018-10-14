tc = int(raw_input())
for ct in range(1,tc+1):
	ans = 0

	b = raw_input().split()
	n = int(b[0])
	s = int(b[1])
	p = int(b[2])
	t = []
	for c in b[3:]:
		t.append(int(c))
	
	ans = 0
	for n in t:
		if n == 0:
			if p == 0:
				ans += 1
			continue
		if n % 3 == 0:
			best = n/3
		else:
			best = n/3 + 1
		if best >= p:
			ans += 1
		elif s > 0:
			best = (n-2)/3 + 2
			if best >= p:
				ans += 1
				s -= 1
		
	print "Case #" + str(ct) + ": " + str(ans)
