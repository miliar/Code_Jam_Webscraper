N = int(raw_input())

for i in xrange(N):
	m0 = 2 # pendiente inicial
	b0 = 0 # ordenada al origen
	x0 = 0 # nodo en X

	s = raw_input().split()
	C = float(s[0])
	F = float(s[1])
	X = float(s[2])

	x1 = (C - b0)/m0
	m1 = m0 + F
	b1 = m1 * (-x1)
	while (X-b0)/m0 > (X-b1)/m1:
		#print 'm0: '+str(m0)
		#print 'b0: '+str(b0)
		#print (X-b0)/m0
		#print (X-b1)/m1

		b0 = b1
		m0 = m1

		x1 = (C - b0)/m0
		m1 = m0 + F
		b1 = m1 * (-x1)

	print 'Case #'+str(i+1)+': '+str((X-b0)/m0)	

