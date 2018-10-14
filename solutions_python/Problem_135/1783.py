in_file = open("1.txt")
t = int(in_file.readline().strip())

for z in range(t):
	choice1 = int(in_file.readline().strip())

	one = []
	two = []

	for i in range(4):
		one.append(in_file.readline().strip().split())
	choice2 = int(in_file.readline().strip())
	for i in range(4):
		two.append( in_file.readline().strip().split() )

	for i in range(4):
		for j in range(4):
			one[i][j] = int(one[i][j])
			two[i][j] = int(two[i][j])

	common = []
	for item in one[choice1 - 1]:
		if item in two[choice2 - 1]:
			common.append(item)


	#print common
	if len(common) == 0:
		end = "Volunteer cheated!"
	elif len(common) == 1:
		end = common[0]
	elif len(common) > 1:
		end = "Bad magician!"

	print "Case #{}: {}".format(z+1,end)

