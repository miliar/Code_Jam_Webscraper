def xor_sum(l):
	s = 0
	for i in xrange(len(l)):
		s^=l[i]
	return s

for c in xrange(int(raw_input())):
	raw_input()
	l = map(int,raw_input().split())
	
	max = 0
	
	possible = False
	
	l.sort()
	
	for i in xrange(1,len(l)):
		patrick = l[:i]
		sean = l[i:]
		if (xor_sum(sean) == xor_sum(patrick)):
			possible = True
			if (sum(sean) > max):
				max = sum(sean)
			
	if (not possible):
		print "Case #"+str(c+1)+": "+"NO"
	else:
		print "Case #"+str(c+1)+": "+str(max)