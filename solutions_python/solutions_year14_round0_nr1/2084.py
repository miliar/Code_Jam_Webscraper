tt=int(raw_input())
for t in range(tt):
	
	print "Case #"+str(t+1)+':',
	no=0
	
	r1=int(raw_input())
	for i in range(4):
		m=raw_input().split()
		if i==r1-1: a=m
	
	r2=int(raw_input())
	for i in range(4):
		m=raw_input().split()
		if i==r2-1:b=m
	
	for i in range(4):
		if a[i] in b:
			no+=1
			v=a[i]
	
	if no==1: print v
	if no==0: print 'Volunteer cheated!'
	if no>1:  print 'Bad magician!'
