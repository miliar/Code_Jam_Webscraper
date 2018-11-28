tn = -1
with open("qwe.in", "r") as myfile:
	for line in myfile:
		tn += 1
		if tn == 0:
			continue
		data = line.split(' ')
		s = data[0]
		k = int(data[1])
		n = len(s)
		a = [0] * n
		can = True
		for i in range(n):
			num = 0
			t = 0
			if i > 0:
				num = a[i-1]
				t = a[i-1]
			if i-k >=0:
				t -= a[i-k]

			if (s[i] == '-' and t%2 == 0) or (s[i] == '+' and t%2 == 1):
				num += 1
				if i >= n-k+1:
					can = False
			#print num
			a[i] = num
		ans = ''
		if not can:
			ans = 'IMPOSSIBLE'
		else:
			ans = a[n-1]
		print 'Case #%s: %s' % (tn , ans)
	


