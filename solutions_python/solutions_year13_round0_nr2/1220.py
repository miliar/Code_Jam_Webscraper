filename = 'B-large.in'
file = open(filename, 'r')
lines = file.read().splitlines()
numTests = int(lines[0])

index = 0
for testNum in range(numTests):
	index += 1
	dimensions = lines[index].split(' ')
	H = int(dimensions[0])
	W = int(dimensions[1])

	rows = []
	cols = []

	for j in range(H):
		index += 1
		row_split = lines[index].split(' ')
		rows.append(map(int,row_split))

		for i in range(W):
			if len(cols) < i+1:
				cols.append([])
			cols[i].append(int(row_split[i]))

	# print "Rows", rows
	# print "Cols", cols
	rowMaxes = [max(row) for row in rows]
	colMaxes = [max(col) for col in cols]

	# print "RMax", rowMaxes
	# print "CMax", colMaxes

	possible = True

	for j in range(H):
		rowMax = rowMaxes[j]
		for i,elem in enumerate(rows[j]):
			if elem < rowMax:
				colMax = colMaxes[i]
				if elem < colMax:
					possible = False
					break
		if not possible:
			break

	if possible:
		print "Case #%d: YES" %(testNum+1)
	else:
		print "Case #%d: NO" %(testNum+1)
