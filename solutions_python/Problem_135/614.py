infile = open("A-small-attempt0.in",'r')
T = int(infile.readline().rstrip())
for x in range(0,T):
	print("Case #"+str(x+1)+": ",end="")
	a = int(infile.readline().rstrip())
	mat = []
	for i in range(4):
		mat.append(infile.readline().rstrip().split(' '))
	b = int(infile.readline())
	mat2 = []
	for i in range(4):
		mat2.append(infile.readline().rstrip().split(' '))
	#print(mat[a-1],mat2[b-1])
	r = set(mat[a-1]) & set(mat2[b-1])

	if len(r) == 0:
		print("Volunteer cheated!")
	elif len(r) == 1:
		for i in r:
			print(i)
	else:
		print("Bad magician!")
