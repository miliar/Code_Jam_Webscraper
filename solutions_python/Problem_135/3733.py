t=int(raw_input())

for i in range(0,t):
	r1=int(raw_input())-1
	l1=[[],[],[],[]]

	for j in range(0,4):
		l=raw_input()
		l1[j]=l.split()

	r2=int(raw_input())-1
	l2=[[],[],[],[]]

	for j in range(0,4):
		l=raw_input()
		l2[j]=l.split()

	count=0
	ans=0
	for j in range(0,4):
		if l2[r2][j] in l1[r1]:
			count=count+1
			ans=int(l2[r2][j])

	if count>=2:
		print "Case #"+str(i+1)+": Bad magician!"
	elif count==1:
		print "Case #"+str(i+1)+": "+str(ans)
	else:
		print "Case #"+str(i+1)+": Volunteer cheated!"


