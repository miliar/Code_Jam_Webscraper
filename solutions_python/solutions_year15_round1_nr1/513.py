import math
for t in range(input()):
	N = input()
	m = map(int,raw_input().strip().split(' '))
	m1 = 0
	m2 = 0
	crate = -1
	for i in range(1,N):
		
		if m[i-1]-m[i] > crate:
			crate = m[i-1]-m[i]
	
	for i in range(1,N):
		if m[i] < m[i-1]:
			m1 += m[i-1]-m[i]
	
	for i in range(N-1):
		m2 += min(crate,m[i])

	print "Case #" + str(t+1) + ": " + str(m1) + " " + str(m2)
