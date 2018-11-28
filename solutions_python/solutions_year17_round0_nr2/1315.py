from __future__ import print_function

def min_digit(l):
	return min(l)

def max_digit(l):
	return max(l)

def is_tidy(l):
	i = 0
	min_d = 1
	max_d = 9
	length = len(l)
	while i < length:
		if(l[i] >= min_d and l[i] <= max_d):
			min_d = l[i]
		else:
			return False
		i+=1
	return True

def count_digits(l):
	return len(l)

def max_tidy(l):
	# print(l)
	length = len(l)
	min_d = 1
	max_d = 9
	index = []
	creep = None
	for i in xrange(length):
		if l[i] > min_d or i == 0:
			index.append(i)
			# print('index: ', index)
		if(l[i] >= min_d and l[i] <= max_d):
			min_d = l[i]
		else:
			creep = i
			break
	new_l = list(l)
	if(len(index) == 1):
		return str(l[0]-1) + '9'*(length-1)
	else:
		s = ''.join(map(str,l))
		x = index[-1]
		# print(x, length)
		return s[0:x] + str(l[x]-1) + '9'*(length-x-1)
	# return str(l[index[-1]-1]) +  


testcases = int(raw_input().strip())
for i in xrange(1,testcases+1):
	n = int(raw_input().strip())
	l = map(int, list(str(n)))
	case_str = 'Case #' + str(i) + ': '
	print(case_str, end='')
	if n < 10:
		print(str(n))
	elif is_tidy(l):
		print(str(n))
	elif max_digit(l) == 1 and min_digit(l) == 0:
		result = '9'*(len(l)-1)
		print(result)
	else:
		result = max_tidy(l)
		# result = '0000090009999'
		while(result and result[0] == '0'):
			result = result[1:]
		
		print(result)
