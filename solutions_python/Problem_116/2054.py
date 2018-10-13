

input_file_name = 'A-large.in'
output_file_name = 'A-large.out'

def check_line(line):
	if (all(map(lambda x: x == 'X' or x == 'T', line))):
		return 'X'
	if (all(map(lambda o: o == 'O' or o == 'T', line))):
		return 'O'
	return None

def check_table(table):
	for i in xrange(4):
		line = table[i]
		result = check_line(line)
		if result is not None:
			return result
	for i in xrange(4):
		line = [l[i] for l in table]
		result = check_line(line)
		if result is not None:
			return result
	line = [table[i][i] for i in xrange(4)]
	result = check_line(line)
	if result is not None:
		return result
	line = [table[i][3-i] for i in xrange(4)]
	result = check_line(line)
	if result is not None:
		return result
	for i in xrange(4):
		if '.' in table[i]:
			return Ellipsis
	return None	


with open(input_file_name) as input_file, open(output_file_name, 'w') as output_file:
	N = int(input_file.readline())
	for T in xrange(N):
		table = []
		for i in xrange(4):
			line = input_file.readline()[:-1]
			table.append(list(line))
		result = check_table(table)
		if result == 'X' or result == 'O':
			output_file.write('Case #{0}: {1} won\n'.format(T+1, result))
		elif result == Ellipsis:
			output_file.write('Case #{0}: Game has not completed\n'.format(T+1))
		else:
			output_file.write('Case #{0}: Draw\n'.format(T+1))
		input_file.readline() # read extra new