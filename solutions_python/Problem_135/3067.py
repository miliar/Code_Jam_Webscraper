f = open("A-small-attempt0.in")
cases = int(f.readline())


# print(cases)
for case in range(cases):
	
	c1 = c2 = []
	pos1 = int(f.readline())
	for i in range(4):
		if (i+1) == pos1:
			c1 = [int(x) for x in f.readline().split()]
			# print (c1)
		else:
			f.readline()

	pos2 = int(f.readline())
	for i in range(4):
		if (i+1) == pos2:
			c2 = [int(x) for x in f.readline().split()]
			# print (c2)
		else:
			f.readline()
	# print (set(c1))
	# print ("-->",set(c1).intersection(set(c2)))
	p = set(c1).intersection(set(c2))
	# print (list(p)[0])
	if (len(p) == 1):
		print ("Case #{}: {}".format(case+1,list(p)[0]))
	else: 
		if (len(p) > 1):
			print ("Case #{}: {}".format(case+1,"Bad magician!"))
		else:
			print ("Case #{}: {}".format(case+1,"Volunteer cheated!"))
