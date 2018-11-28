t = int(raw_input())
clap = []

for i in range(t):
	smax, k = raw_input().split()
	l = len(k)

	ans = 0
	a = 0	
	for j in range(l):
		a = a + int(k[j])
		if (a >= (j+1)):
			ans = ans + 0
		else:
			ans = ans + 1
			a = j+1
	clap.append(ans)
			

for i in range(t):
	print "Case #%d: %d" %((i+1), clap[i])



		