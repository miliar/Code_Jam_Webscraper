def mat(f):
	l = []
	for i in xrange(4):
		t = raw_input().split()
		if i == f:
			l = t
	return [int(i) for i in l]
	

N = int(raw_input())

for i in xrange(N):
	f0 = int(raw_input())
	m0 = mat(f0-1)
	f1 = int(raw_input())
	m1 = mat(f1-1)

	c = 0
	n = 0
	for j in m0:
		c += m1.count(j)
		if m1.count(j):
			n = j

	if c == 0:
		print 'Case #'+str(i+1)+': Volunteer cheated!'
	elif c == 1:	
		print 'Case #'+str(i+1)+': '+str(n)
	else:
		print 'Case #'+str(i+1)+': Bad magician!'

