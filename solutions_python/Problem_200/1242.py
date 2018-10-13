# code jam 2016 qualification A
# N, 2N, 3N... until all digits used otherwise print 'INSOMNIA'
# input file has num of test cases followed by a new N on each line

def first_bad_pos(num):
	# returning False means number is tidy
	# otherwise returns first index of descending
	num_string = str(num)
	if len(num_string) == 1:
		return -1
	for i in range(len(num_string)-1):
		if int(num_string[i]) > int(num_string[i+1]):
			return i
	return -1

def transform(num, pos):
	# gives position of first descending (not zero)
	num_string = str(num)
	result = ''
	for i in range(len(num_string)):
		if i < pos:
			result += num_string[i]
		elif i == pos:
			result += str(int(num_string[i]) - 1)
		else:
			result += '9'
	return int(result)

def zero_transform(num):
	# returns 9s
	num_string = str(num)
	result = ''
	for i in range(len(num_string)-1):
		result += '9'
	return int(result)

t = int(raw_input()) # this is the number of test cases
for i in xrange(1, t+1):
	number = int(raw_input())
	while first_bad_pos(number) != -1:
		if str(number)[:2] == '10':
			number = zero_transform(number)
		else:
			number = transform(number, first_bad_pos(number))
	
	print  "Case #{}: {}".format(i, number)
	
