import math
def bottom_half_parse_minus(first_digit, trailing_number_length):
	return int(first_digit * math.pow(10,trailing_number_length)) - 1
def concat_number_list(l):
	output = 0
	for i in range(len(l)):
		output = output * 10
		output += int(l[i])
	return output
def bottom_half_parse(l, trailing_number_length):
	return int(concat_number_list(l) * math.pow(10, trailing_number_length))
def bottom_half_parse_add(l, trailing_number_length):
	return bottom_half_parse(l, trailing_number_length) + bottom_half_parse_minus
f = open('B-small-attempt2.in', 'r')
T = int(f.readline())
for i in range(T):
	line1 = f.readline().rsplit()[0]
	line = list(str(line1))
	idx = 0
	status = [] # 1 = great, 0 = equal
	if len(line) == 1:
		print 'Case #' + str(i+1) + ': ' + str((line[0]))
	else:
		solved = 0
		while idx < len(line)-1:
			foo = int(line[idx])
			bar = int(line[idx+1])
			if foo < bar:
				status.append(1)
			elif foo == bar:
				status.append(0)
			else:
				# find the last occurrence of 1 = y
				if 1 not in status:
					# if not found, decrease first digit (idx 0) by 1
					first_digit = int(line[0]) 
					trailing_number_length = len(line) - 1
					print 'Case #' + str(i+1) + ': ' + str(bottom_half_parse_minus(first_digit, trailing_number_length))
					solved = 1
					break
					# and all subsequent to 9
				# else decrease digit of idx y+1 by 1
				else:
					idx_1 = status.index(1) + 1
					a = bottom_half_parse(line[:idx_1], len(line)-idx_1)
					first_digit = int(line[idx_1])
					trailing_number_length = len(line) - idx_1 -1
					b = bottom_half_parse_minus(first_digit, trailing_number_length)
					print 'Case #' + str(i+1) + ': ' + str(a+b)
					solved = 1
					break
				# and all subsequent to 9
			idx = idx+1
		if solved == 0:
			print 'Case #' + str(i+1) + ': ' + line1