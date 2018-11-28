answers =[]
test_cases = int(raw_input())
for case in range(test_cases):
	grid1 = []
	grid2 = []
	an1 = int(raw_input())
	for i in range(4):
		grid1.append([ int(x) for x in raw_input().split()])
	an2 = int(raw_input())
	for i in range(4):
		grid2.append([ int(x) for x in raw_input().split()])
	an1 -= 1
	an2 -= 1
	set1 = set(grid1[an1])
	set2 = set(grid2[an2])
	u = set1.intersection(set2)
	if len(u) == 0:
		answers.append("Case #%d: Volunteer cheated!"%(case+1,))
	elif len(u) > 1:
		answers.append("Case #%d: Bad magician!"%(case+1,))
	else:
		answers.append("Case #%d: %d"%(case+1,u.pop()))
for x in answers:
	print x

