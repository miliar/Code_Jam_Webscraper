def is_flip_worthy(s):
	s_length = len(s)
	count = 0
	for i in range(s_length):
		if s[i] == '-':
			count += 1
		if count > int(s_length/2):
			return True
	return False

def get_flipped(s):
	s_length = len(s)
	count = 0
	ret_str = ''
	for i in range(s_length):
		if s[i] == '-':
			ret_str += '+'
		else:
			ret_str += '-'
	return ret_str

def is_infinite(s):
	s_length = len(s)
	for i in range(s_length):
		if s[i] == '-':
			return True
	return False

def flip_count(s, k):

	# default return value is -1, INFINITE
	ret_val = -1
	# length of the pattern
	s_length = len(s)
	# check data validity
	if s_length < k:
		return ret_val

	# set return value to 0
	ret_val = 0
	for i in range(s_length - k + 1):
		before = s
		s_subset = s[i:i+k]
		#print("index : {}, value : {}".format(i, s_subset))
		if s_subset[0] == '-':
			s = s[:i] + get_flipped(s_subset) + s[i+len(s_subset):]
			ret_val += 1
		#print("before : {}, after : {}".format(before, s))

	for i in range(s_length - k, -1, -1):
		before = s
		s_subset = s[i:i+k]
		#print("index : {}, value : {}".format(i, s_subset))
		if s_subset[len(s_subset)-1] == '-':
			s = s[:i] + get_flipped(s_subset) + s[i+len(s_subset):]
			ret_val += 1
		#print("before : {}, after : {}".format(before, s))

	if is_infinite(s):
		return -1

	return ret_val

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  s, k = input().split(" ")  # read a string and integer
  fc = flip_count(s, int(k))
  if fc >= 0:
  	print("Case #{}: {}".format(i, fc))
  else:
  	print("Case #{}: IMPOSSIBLE".format(i))