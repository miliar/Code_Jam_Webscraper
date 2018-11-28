T=int(raw_input())

for ca in range(T):
	ans = 0
	line = raw_input()
	smax, s =  line.split(' ')
	smax = int(smax)
	sum1 = 0
	a = 0
	for i in range(smax+1):
		a = s[i]
		a = int(a)
		if a != 0 and i > sum1:
			ans += i-sum1
			sum1 = i
		sum1 += a
	print "Case #%d: %d" %(ca+1, ans)