import sys

f = open(sys.argv[1])

n = int(f.readline())
for testcase in range(1, n+1):
	s = f.readline().split()
	C = {}
	D = {}
	for i in range(int(s.pop(0))):
		x = s.pop(0)
		C[(x[0], x[1])] = x[2]
		C[(x[1], x[0])] = x[2]
		
	for i in range(int(s.pop(0))):
		x = s.pop(0)
		try: D[x[0]].append(x[1])
		except: D[x[0]] = x[1]
		try: D[x[1]].append(x[0])
		except: D[x[1]] = x[0]
	
	s.pop(0)
	S = s.pop(0)
	
	x = []
	for s in S:
		x.append(s)
		
		while True:			
			if len(x) < 2: break
			c = 0
			
			if C.has_key((x[-1], x[-2])):
				y = C[(x[-1], x[-2])]
				x.pop()
				x.pop()
				x.append(y)
				c = 1
				
			if D.has_key(x[-1]):
				for y in x[:-1]:
					if y in D[x[-1]]:
						x = []
						c = 1
						break

			if c==0: break
	
	c = ', '.join(x)
	
	print 'Case #%d: [%s]' % (testcase, c)
