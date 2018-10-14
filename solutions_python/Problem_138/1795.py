t = int(raw_input())
k = 1
while t>0:
	N = int(raw_input())
	a = raw_input().split()
	a = map(float, a)
	b = raw_input().split()
	b = map(float, b)
	c = sorted(a)
	l = str(k)
	sorted(b, reverse=True)
	count = 0
	for i in b:
		for j in c:
			if j>i:
				c.remove(j)
				count += 1
				break
	
	d = sorted(a, reverse=True)
	for p in b:
		for q in d:
			if q<p:
				d.remove(q)
				break
	
	print("Case #" + l + ": %d %d" % (count, len(d)))
	
	k += 1
	t -= 1