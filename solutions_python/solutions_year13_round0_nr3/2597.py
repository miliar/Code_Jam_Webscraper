import math

filename = 'C-small-attempt1'

def is_palindrome(m):
	s = str(m)
	n = len(s)
	res = True
	for i in range(n / 2):
		if s[i] != s[n - i - 1]:
			res = False

	return res



if __name__ == "__main__":
	test_cases = open(filename + '.in', 'r')
	# Code for preprocessing/reading from file here.
	root_intervals = []

	test_cases.readline()
	for line in test_cases:
		root_intervals.append(tuple([math.sqrt(int(x)) for x in line.split()]))

	out_file = open(filename + '.out', 'w')

	for i in range(len(root_intervals)):
		# Code for processing data here.
		squares = []
		for j in range(int(math.ceil(root_intervals[i][0])),
			           int(math.floor(root_intervals[i][1]) + 1)):
			squares.append((j, j ** 2))

		num_fair_and_square = 0
		for square in squares:
			if is_palindrome(square[0]) and is_palindrome(square[1]):
				num_fair_and_square += 1

		# Code for writing to file here.
		s = 'Case #{}: {}\n'.format(i + 1, num_fair_and_square)
		print s
		out_file.write(s)


	# print is_palindrome('5')
	# print is_palindrome('0')
	# print is_palindrome('11')
	# print is_palindrome('22')
	# print is_palindrome('121')
	# print is_palindrome('1216121')
	# print is_palindrome('3443')
	# print is_palindrome('12345654321')
	# print
	# print is_palindrome('10')
	# print is_palindrome('23')
	# print is_palindrome('1211321')
	# print is_palindrome('12345765654321')