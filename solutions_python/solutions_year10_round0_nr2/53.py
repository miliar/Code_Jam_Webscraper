import fractions
tn = int(raw_input())
for ti in range(tn):
	a = raw_input().split()
	a[0] = int(a[0])
	for i in range(1,a[0]+1):
		a[i] = int(a[i])
	g = abs(a[1] - a[2])
	for i in range(1,a[0] + 1):
		for j in range(i + 1, a[0] + 1):
			g = fractions.gcd(g, abs(a[i] - a[j]))
	print "Case #%d: %d" %(ti + 1, (g - a[1] % g)%g)
