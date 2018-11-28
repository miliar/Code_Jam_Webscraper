def split_line(line, sep=' '):
	numbers = []
	num = ''

	for char in line:
		if char == sep:
			if num != '':
				numbers.append(int(num))
			num = ''
		else:
			num += char

	if num != '':
		numbers.append(int(num))
	num = ''

	return numbers

def compare_rows(first_row, second_row):
	similarities = 0
	value = 0

	for x in xrange(1, 5):
		if first_row[x-1] in second_row:
			similarities += 1
			value = first_row[x-1]

	return similarities, value

if __name__ == '__main__':
	f = open('in.in', 'r')#Open input file

	out = open('out.out', 'w')#Open output file

	test_cases = int(f.readline().strip())# Get number of test cases
	

	for n in xrange(1, test_cases+1):

		row_1 = int(f.readline().strip())
		first_row = []

		for x in xrange(1, 5):
			if x == row_1:
				first_row = split_line(f.readline().strip())
			else:
				f.readline()

		row_2 = int(f.readline().strip())
		second_row = []

		for x in xrange(1, 5):
			if x == row_2:
				second_row = split_line(f.readline().strip())
			else:
				f.readline()

		answer, value = compare_rows(first_row, second_row)

		if answer == 0:
			case = 'Case #{0}: {1}\n'.format(n, 'Volunteer cheated!')
			out.write(case)
		elif answer == 1:
			case = 'Case #{0}: {1}\n'.format(n, value)
			out.write(case)
		else:
			case = 'Case #{0}: {1}\n'.format(n, 'Bad magician!')
			out.write(case)