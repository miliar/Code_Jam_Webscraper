t = int(raw_input())
for x in range(t):
	r,c = map(int,raw_input().split())
	m = ['' for j in range(r)]
	for i in range(r):
		row = raw_input()
		m[i] = row
		
	
	for i in range(r):
		for j in range(c):
			if m[i][j] >= 'A' and m[i][j] <= 'Z':
				temp = m[i][j:]
				m[i] = m[i][:j].replace('?',m[i][j]) + temp

	
	for i in range(r):
		curr = None
		for j in range(c):
			#print m[i][j],curr
			if m[i][j] >= 'A' and m[i][j] <= 'Z':
				curr = m[i][j]
			elif m[i][j] == '?' and curr!=None:
				#print "yes"
				m[i] = m[i].replace('?',curr)			

				
				
				
	curr = None
	for i in range(r):
		
		if m[i] != '?'*c:
			curr = m[i]
		elif m[i] == '?'*c and curr!=None:
			m[i] = curr
	
	curr = None		
	for i in range(r):
		if m[r-i-1] != '?'*c:
			curr = m[r-i-1]
		elif m[r-i-1] == '?'*c and curr!=None:
			m[r-i-1] = curr
			
	print 'Case #{}:'.format(x+1)
	for i in range(r):
		print m[i]
			
			