



f = open("A-small-attempt4.in")
o = open('output','w')
cases = f.readline()

cases=int(cases)


for i in range(cases):
	rows1 = {}
	rows2 = {}
	visited = {}
	count_match = 0
	sol = -1
	ans1 = f.readline()
	ans1 = int(ans1)
	row1 = f.readline().split()
	row2 = f.readline().split()
	row3 = f.readline().split()
	row4 = f.readline().split()
	rows1[1] = row1
	rows1[2] = row2
	rows1[3] = row3
	rows1[4] = row4
	ans2 = f.readline()
	ans2 = int(ans2)
	row1 = f.readline().split()
	row2 = f.readline().split()
	row3 = f.readline().split()
	row4 = f.readline().split()
	rows2[1] = row1
	rows2[2] = row2
	rows2[3] = row3
	rows2[4] = row4

	for num in rows1[ans1]:
		visited[num] = 1
	for num2 in rows2[ans2]:
		if(num2 in visited):
			count_match += 1
			sol = num2

	if(count_match == 1):
		o.write('Case #'+str(i+1)+': '+sol+'\n')
	elif(count_match >=2):
		o.write('Case #'+str(i+1)+': Bad magician!\n')
	else:
		o.write('Case #'+str(i+1)+': Volunteer cheated!\n')

	





























