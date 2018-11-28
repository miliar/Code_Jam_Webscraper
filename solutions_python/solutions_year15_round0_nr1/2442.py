T = raw_input()
110011
for z in range(int(T)):
	friend = 0
	s = raw_input().split()
	l = map(int, list(s[1]))
	s = int(s[0])
	standing = 0
	
	for i in range(s+1):
		if standing >= i:
			standing += l[i]
		else:
			friend += (i - standing)
			standing += l[i] + i - standing
		# print standing
	print 'Case #%d: %d'%(z+1, friend)
