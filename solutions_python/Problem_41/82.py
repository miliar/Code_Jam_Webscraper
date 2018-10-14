#!/usr/bin/python

import sys

# main function
# write code from here
def process(input, output):
	nb = int(input.readline().rstrip())

	for val in range(1, nb+1):
		digits = []
		number = []
		n = input.readline().rstrip()
		prev = 0
		ind = -1

		for i in n:
			number.append(i)

		for i in range(len(number)-2, -1, -1):
			prev = number[i+1]
			if number[i] < prev:
				ind = i
				break

		# special case
		if ind == -1:
			number.insert(0, 0)
			ind = 0

		# can be optimized
		for i in range(ind, len(number)):
			digits.append(number[i])
		digits.sort()

		for i in range(1, len(digits)):
			if digits[i] != '0' and digits[i] > number[ind]:
				number[ind] = digits[i]
				digits.remove(digits[i])
				break

		for i in range(len(digits)):
			number[ind+i+1] = digits[i]

		n = ""
		for x in number:
			n += str(x)

		output.write('Case #%d: %s\n' %(val, n))

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print "Need file as argument"
		sys.exit(1)

	input_file = sys.argv[1]

	# open the file
	input_handler = open(input_file, 'r')
	output_handler = open(input_file + '.out', 'w+')

	process(input_handler, output_handler)

	# close files
	input_handler.close()
	output_handler.close()
