f = open('A-small-attempt0.in')
fw = open('A-small-output.txt', 'w')

cases = int(f.readline())
for case in range(cases):
	grid_1 = []
	grid_2 = []
	row_1 = int(f.readline()) - 1
	for i in [1, 2, 3, 4]:
		grid_1.append(f.readline().split())
	row_2 = int(f.readline()) - 1
	for i in [1, 2, 3, 4]:
		grid_2.append(f.readline().split())
	match = []
	for s1 in grid_1[row_1]:
		for s2 in grid_2[row_2]:
			if (s1 == s2):
				match.append(s1)
	if len(match) == 1:
		ans = match[0]
	elif len(match) > 1:
		ans = 'Bad magician!'
	else:
		ans = 'Volunteer cheated!'
	print ans
	fw.write('Case #' + str(case + 1) + ': ' + ans + '\n')

fw.close()
f.close()
