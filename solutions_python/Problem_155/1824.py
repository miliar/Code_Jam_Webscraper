
t = int(raw_input())
sol = []

for i in xrange(t):
	ans = 0
	nstand = 0
	smax, s = raw_input().split()
	for j,n in enumerate([int(x) for x in s]):
		if n > 0:
			if nstand >= j:
				nstand += n
			else:
				ans += j-nstand
				nstand = j+n
	sol.append("Case #" + str(i+1) + ": " + str(ans))

for line in sol:
	print line