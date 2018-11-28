def answer(row1, row2):
	same = row1.intersection(row2)
	if len(same) == 1:
		return same.pop()
	elif len(same) < 1:
		return 'Volunteer cheated!'
	else:
		return 'Bad magician!'


with open('A-small-attempt1.out', 'w') as y:
	with open('A-small-attempt1.in','r') as z:
		num_cases = int(z.readline().strip())
		for i in range(num_cases):
			selection1 = int(z.readline().strip())-1
			grid1 = []
			grid1.append(set([int(x) for x in z.readline().strip().split(' ')]))
			grid1.append(set([int(x) for x in z.readline().strip().split(' ')]))
			grid1.append(set([int(x) for x in z.readline().strip().split(' ')]))
			grid1.append(set([int(x) for x in z.readline().strip().split(' ')]))
			selection2 = int(z.readline().strip())-1
			grid2 = []
			grid2.append(set([int(x) for x in z.readline().strip().split(' ')]))
			grid2.append(set([int(x) for x in z.readline().strip().split(' ')]))
			grid2.append(set([int(x) for x in z.readline().strip().split(' ')]))
			grid2.append(set([int(x) for x in z.readline().strip().split(' ')]))
			y.write("Case #%s: %s\n" %(i+1, answer(grid1[selection1], grid2[selection2])))
			
