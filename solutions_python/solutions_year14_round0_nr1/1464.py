file = open('A-small-attempt0.in', 'r')
test_count = int(file.readline().rstrip('\n'))

# TODO: change this later
line_array = []
line = file.readline()
while line != '':
	line_array.append(line.rstrip('\n'))
	line = file.readline()
file.close()

output_file = open('p1-output.txt', 'w+')
all = {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16'}

def getPossibilities(current_possibilities, row):
	new_set = set()
	for i in row:
		if i in current_possibilities:
			new_set.add(i)
	return new_set

for i in xrange(test_count):
	# Get first board row number
	fbrn = line_array[i * 10]
	row = line_array[i * 10 + int(fbrn)].split()
	soln = getPossibilities(all, row)
	sbrn = line_array[i * 10 + 5]
	row = line_array[i * 10 + 5 + int(sbrn)].split()
	soln = getPossibilities(soln, row)
	string_solution = 'Case #' + str((i + 1)) + ': '
	if (len(soln) == 0):
		output_file.write(string_solution + 'Volunteer cheated!\n')
	elif (len(soln) > 1):
		output_file.write(string_solution + 'Bad magician!\n')
	else:
		output_file.write(string_solution + soln.pop() + '\n')
