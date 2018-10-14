for tmp in xrange(1,input()+1):
	a = raw_input()
	for i in xrange(len(a)-1):
		if a[i]>a[i+1]:
			while i > 0 and a[i] == a[i-1]:
				i-=1
			a = long(a[:i+1]+'0'*(len(a)-i-1))-1
			break
	print 'Case #%d:'%tmp,a	
