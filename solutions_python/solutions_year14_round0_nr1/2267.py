for t in range(input()):
	r1=input()
	for i in range(4):
		r=raw_input().strip().split()
		if i == r1-1:
			s1=r
	r2=input()
	for i in range(4):
		r=raw_input().strip().split()
		if i == r2-1:
			s2=r
	cm=-1
	cn=0
	for i in s1:
		if i in s2:
			cm=i
			cn+=1
	if cn==0:
		print "Case #"+str(t+1)+":","Volunteer cheated!"
	elif cn>1:
		print "Case #"+str(t+1)+":","Bad magician!"
	else:
		print "Case #"+str(t+1)+":",cm