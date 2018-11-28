with open('A-small-attempt0.in') as f:
	out = open('out','w')
	case = int(f.readline())
	for c in range(case):
		matrix1 = []
		row1 = int(f.readline()) - 1
		for i in range(4):
			matrix1.append(f.readline().strip().split(' '))
		matrix2 = []
		row2 = int(f.readline()) - 1
		for i in range(4):
			matrix2.append(f.readline().strip().split(' '))
		intersect = set(matrix1[row1]).intersection(matrix2[row2])
		if len(intersect) > 1:
			out.write("Case #%d: Bad magician!\n" % (c+1))
		elif len(intersect) == 1:
			out.write("Case #%d: %s\n" % (c+1, intersect.pop()))
		elif len(intersect) < 1:
			out.write("Case #%d: Volunteer cheated!\n" % (c+1))
		out.flush()