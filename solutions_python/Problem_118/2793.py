def square_root(num):
	x = num
	y = (x + num // x) // 2
	while y < x:
		x = y
		y = (x + num // x) //2
	return x

def is_fair_and_square(num):
	return (str(num) == str(num)[::-1]) and (square_root(num)**2 == num) and (str(square_root(num)) == str(square_root(num))[::-1])
	

def find_fair_and_square(lower_bound, upper_bound):
	i = lower_bound
	fairs_and_squares = []
	while i <= upper_bound:
		if is_fair_and_square(i):
			fairs_and_squares.append(i)
		i = i + 1
	return len(fairs_and_squares)

from sys import argv
script, input_file, output_file = argv

input_data = open(input_file)
output_data = open(output_file, 'w')
num_cases = int(input_data.readline())
i = 0

while i < num_cases:
	input_line = input_data.readline().split()
	lower_bound = input_line[0]
	upper_bound = input_line[1]
	result = find_fair_and_square(int(lower_bound), int(upper_bound))
	output_data.write("Case #%s:  %d\n" % (i + 1, result))
	i = i + 1
output_data.close()
	