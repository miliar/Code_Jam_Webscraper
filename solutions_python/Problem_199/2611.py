for tmp in xrange(1,input()+1):
	s,x = raw_input().split()
	x = int(x)
	s = list(s)
	count = 0
	while('-' in s):
		i = s.index('-')
		if i+x>len(s):			
			break				
		for j in xrange(x):
			if s[i+j] == '-':
				s[i+j] = '+'
			else:
				s[i+j] = '-'
		count+=1
	if '-' in s:
		print 'Case #%d: IMPOSSIBLE'%tmp
	else:
		print "Case #%d:"%tmp,count

	
