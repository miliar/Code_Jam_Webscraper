import array
import string
N = raw_input()
N = int(N)
T = 0
while(T < N):
	T = T + 1
	p1 = int(raw_input()) - 1
	#print p1
	s1 = []
	s2 = []
	for i in range(0, 4):
		x = ()
		s = raw_input() 
		for j in range(0, 4):
			if j < 3:
				c = s.index(' ')
				x = x + (int(s[:c]),)
				s = s[c+1:]
			else:
				x = x + (int(s),)
		#print x 
		s1.append(x)
	p2 = int(raw_input()) - 1
	#print p2
	for i in range(0, 4):
		x = ()
		s = raw_input() 
		for j in range(0, 4):
			#print s
			if j < 3:
				c = s.index(' ')
				#print s 
				#print c
				#print '/ ' + s[:c] + '/ '
				x = x + (int(s[:c]),)
				s = s[c+1:]
			else:
				x = x + (int(s),)
		#print x 
		s2.append(x)
	res = 0
	r = 0
	#print s1[p1]
	#print s1[p2]
	#print s1
	#print s2
	for m in s1[p1]:
		if m in s2[p2]:
			res = res + 1
			r = m

	if res < 1:
		print 'Case #{0}: Volunteer cheated!'.format(T)
	elif res > 1:
		print 'Case #{0}: Bad magician!'.format(T)
	else:
		print 'Case #{0}: {1}'.format(T, r)
