import os

T = int(raw_input(''))
for t in range(0, T):
	N = int(raw_input(''))
	m = raw_input('').split(' ')

	y = 0
	max = 0
	for n in range(0, N):
		try:
			m1 = int(m[n])
			m2 = int(m[n+1])
			if m1>m2:
				m3 = m1-m2
				if m3>max:
					max = m3
				y += m3
		except:
			None
	z = 0
	for n in range(0, N):
		m1 = int(m[n])
		if m1>0:
			if (n+1)==N:
				break
			if m1>max:
				z += max
			else:
				z += m1
	print 'Case #'+str(t+1)+': '+str(y)+' '+str(z)
