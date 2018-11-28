t=int(raw_input())
for i in range(t):
	choice1=int(raw_input())
	mat1=[]
	for j in range(4):
		l=[int(x) for x in raw_input().split()]
		mat1.append(l)
		l=[]
	choice2=int(raw_input())
	mat2=[]
	for k in range(4):
		l=[int(x) for x in raw_input().split()]
		mat2.append(l)
		l=[]
	x=mat1[choice1-1]
	y=mat2[choice2-1]
	z=list(set(x).intersection(y))
	if len(z)==1:
		print "Case #%d: %d" % (i+1,z[0])
	elif len(z)>1:
		print "Case #%d: Bad magician!" %(i+1)
	elif len(z)==0:
		print "Case #%d: Volunteer cheated!" %(i+1)