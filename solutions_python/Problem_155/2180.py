def run_all(input_name, output_name):
	input_file = open(input_name, 'r')
	lines = input_file.readlines()
	input_file.close()
	output = ''
	for i, line in enumerate(lines[1:]):
		output += 'Case #' + str(i + 1) + ': ' + str(solve(line.split()[1])) + '\n'
	output = output[:-1]
	output_file = open(output_name, 'w')
	output_file.write(output)
	output_file.close()

def solve(audience):
	standing = 0
	extra = 0
	for shyness, num in enumerate(audience):
		if int(num) > 0 and shyness > standing:
			extra += shyness - standing
			standing = shyness
		standing += int(num)
	return extra

if __name__ == '__main__':
	run_all('A-large.in', 'A-large.out')
