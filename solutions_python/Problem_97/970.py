T = int(raw_input().strip())
for i in xrange(T):
	included = []
	numRecycled = 0
	A,B = [int(num) for num in raw_input().strip().split()]
	n = A
	while n <= B:
		r = str(n)	
		size_r = len(r)
		if size_r > 1:
			for size in xrange(size_r-1):	
				p1 = r[0:(size + 1)]
				p2 = r[(size+1):]
				if p2[0] == '0':
					continue
				recycled = p2 + p1

				m = int(recycled)
				if (m >= A) and (m <= B) and (n != m) and (not ((m,n) in included)) and (not ((n,m) in included)) and (m > n):
					included.append((n,m))
					
		n = n + 1
	print 'Case #%s: %s' % ((i+1),len(included))