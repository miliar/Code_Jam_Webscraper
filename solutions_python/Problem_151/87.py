
t = int(raw_input())
for ti in range(t):
	(m,n) = map(int,raw_input().split())
	s = []
	for i in range(m):
		x = raw_input()
		s.append(x)

	a = [0]*(m+1)
	qmx = 0
	qmxc = 0
	while a[m]==0:
		a[0]+=1
		for i in range(m):
			a[i+1] += a[i]/n
			a[i] %= n
		q = 0
		for i in range(n):
			w = set()
			for j in range(m):
				if a[j] == i:
					for k in range(len(s[j])+1):
						w.add(s[j][0:k])
			q += len(w)
		if q > qmx:
			qmx = q
			qmxc = 0
		if q == qmx:
			qmxc = (qmxc+1)%1000000007


	print "Case #%d: %d %d" % ( ti+1, qmx, qmxc )

