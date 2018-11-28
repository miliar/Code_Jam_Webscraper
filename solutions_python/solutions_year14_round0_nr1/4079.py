

lines = open('A-small-attempt0.in', 'r')

array = []
for line in lines:
	# print line
	array.append(line)

lines.close()

# num_line = len(array)

cases = array[0]

for i in range(int(cases)):
	row1 = int(array[i * 10 + 1])
	# print array[i * 10 + 1 + row1].split()
	target1 = set(array[i * 10 + 1 + row1].split())
	row2 = int(array[i * 10 + 6])
	# print array[i * 10 + 6 + row2].split()
	target2 = set(array[i * 10 + 6 + row2].split())

	intersect = target1.intersection(target2)

	result = list(intersect)
	size = len(result)

	if size == 1:
		print 'Case #' + str(i + 1) + ': ' + str(result[0])
	elif size > 1:
		print 'Case #' + str(i + 1) + ': ' + 'Bad magician!'
	else:
		print 'Case #' + str(i + 1) + ': ' + 'Volunteer cheated!'
	