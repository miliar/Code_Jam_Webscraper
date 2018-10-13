def test_for(letter, testcase):

	columns = [''] * 4

	for i in range(len(testcase)): # Rows

		if 'T' in testcase[i]:
			testcase[i] = testcase[i].replace('T', letter)

		for j in range(len(testcase[i])): # Letters
			columns[j] += testcase[i][j]
		
		if testcase[i] == (letter * 4):
			return True

	if (letter * 4) in columns:
		return True

	LRdiagonal = testcase[0][0] + testcase[2][2] + testcase[3][3] + testcase[3][3]

	if (letter * 4) in LRdiagonal:
		return True

	RLdiagonal = testcase[0][3] + testcase[1][2] + testcase[2][1] + testcase[3][0]

	if (letter * 4) in RLdiagonal:
		return True

	return False


input_file = open('in1.in', 'r+')
input_data = input_file.read()
input_file.close()

input_data = input_data.split('\n\n')


for i in range(len(input_data)):
	input_data[i] = input_data[i].split('\n')


testcases_number = int(input_data[0][0])
input_data[0].pop(0)
input_data.pop()

print "Input data:", input_data



case = 1
output = ''

for testcase in input_data:

	x_won = test_for('X', testcase[:])
	o_won = test_for('O', testcase[:])

	not_finished = False

	for row in testcase:
		if '.' in row:
			not_finished = True
			break

	if x_won:
		output += "Case #%i: X won\n" % case
	elif o_won:
		output += "Case #%i: O won\n" % case
	elif not_finished:
		output += "Case #%i: Game has not completed\n" % case
	else:
		output += "Case #%i: Draw\n" % case

	case += 1

print output

output_file = open('out1.out', 'r+')
output_file.write(output)
output_file.close()
