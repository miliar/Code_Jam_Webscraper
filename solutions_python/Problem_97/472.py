t = int(raw_input())
for i in range(1,t+1):
	r = raw_input().split(" ")
	a = int(r[0])
	b = int(r[1])
	s = {}
	n = 0
	for j in range(a,b+1):
		m = str(j)
		for k in range(1,len(m)):
			u = m[k:] + m[0:k]
			if u[0] == '0':
				continue
			if a <= int(u) <= b and int(u) > j:
				if (j,int(u)) in s:
					continue
				s[(j,int(u))] = True
				n += 1
	print "Case #" + str(i) + ": " + str(n)
