T = int(raw_input())

for c in xrange(T):
	need = 0
	standing = 0
	N,sh = raw_input().split()
	for k,s in enumerate(sh):
		s = int(s)
		#print 'shyness',k,'people',s
		if standing >= k:
			standing += s
		else:
			bring = k - standing
			standing += s + bring
			need += bring
	print 'Case #'+str(c+1)+':',need
