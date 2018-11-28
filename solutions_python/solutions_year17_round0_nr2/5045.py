def tidy_number(str):
	for index in range(len(str) - 1):
		if str[index] > str[index + 1]:
			return False
	return True

# print tidy_number('11111111111111111111111111111111111')

sample = 'tidy_sample.txt'
small = 'tidy_small.txt'


def file_reader(file):
	file = open(file, 'r')
	a_list = file.read().split('\n')[1:]
	return a_list


def last_tidy_number(string):
	limit = int(string)
	while limit > 0:
		if limit > 1000000:
			return 0
		if tidy_number(str(limit)):
			return limit
		limit -= 1


def solution(file, output_file):
	a_file = open(output_file, 'w')
	for index, test in enumerate(file_reader(file)):
		print 'Case #%s: %s' % (index + 1, last_tidy_number(test))
		a_file.write('Case #%s: %s\n' % (index + 1, last_tidy_number(test)))
	a_file.close()

# solution(sample, 'tidy_output_sample.txt')
solution(small, 'tidy_output_small.txt')