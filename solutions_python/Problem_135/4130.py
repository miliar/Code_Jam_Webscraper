f = open('A-small-attempt0.in')

num_cases = int(f.readline())

def handleArrangement():
	row_num = int(f.readline())
	# print row_num
	arrangement = []
	for i in range(0, 4):
		row_in = f.readline().split(' ')
		row = []
		for j in range(0, 4):
			row.append(int(row_in[j]))
		arrangement.append(row)
	return getRowValues(row_num, arrangement)

def getRowValues(n, arrangement):
	# print arrangement
	row_values = []
	for i in range(0, 4):
		row_values.append(arrangement[n-1][i])
	# print row_values
	return row_values

def pickValue(row1, row2):
	values = []
	hash = {}
	for i in range(0, 4):
		if not row1[i] in hash:
			hash[row1[i]] = 1
		else:
			print "Bad magician!"

	for i in range(0, 4):
		if row2[i] in hash:
			values.append(row2[i])

	if len(values) == 0:
		print "Volunteer cheated!"
	elif len(values) > 1:
		print "Bad magician!"
	else: 
		print values[0]
		


for i in range(0, num_cases):
	print "Case #" + str(i+1) + ": ",
	row1 = handleArrangement()
	row2 = handleArrangement()
	pickValue(row1, row2)

