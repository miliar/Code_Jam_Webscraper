

def is_tidy(number):
	return all(number[i] <= number[i+1] for i in xrange(len(number)-1))


def run():
	input_file = open('small.in', 'r')
	output_file = open('smalltidy.out', 'w')
	first_line = input_file.readline() # read the first line of the content of the small.in file
	T = int(first_line) # convert the string file to integer
	for no in xrange(1, T+1):
		number = long(next(input_file))
		for current in xrange(number, 0 ,-1):
			if is_tidy(str(current)):
				output_file.write('Case #{}: {}\n'.format(no, current))
				print('Case #{}: {}'.format(no, current))
				break


run()