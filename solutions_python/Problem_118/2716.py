from math import sqrt

def is_pal(n):

	n = str(n)
	return n == n[::-1]

input_file = open('in3.in', 'r+')
input_data = input_file.read()
input_file.close()

input_data = input_data.split('\n')

testcases_number = int(input_data[0])
input_data.pop(0)

input_data = input_data[:testcases_number]

print input_data

case = 1
output = ''

for testcase in input_data:

	endpoints = testcase.split()
	number_range = range(int(endpoints[0]), int(endpoints[1]) + 1)

	total = 0

	for n in number_range:

		root = sqrt(n)

		if root.is_integer() and is_pal(n) and is_pal(int(root)):
			total += 1

	output += "Case #%i: %i\n" % (case, total)
	case += 1

print output

output_file = open('out3.out', 'r+')
output_file.write(output)
output_file.close()