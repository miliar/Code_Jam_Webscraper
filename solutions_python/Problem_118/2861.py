import math

def find_fair_square(path="input.txt"):
	input_file = open(path)
	result = open("output.txt", "w")
	cases = int(input_file.readline())
	for i in range(cases):
		s = input_file.readline()
		start, stop = s.split()
		count = count_fair_square(int(start), int(stop))
		output = "Case #%s: %s\n" % (i+1, count)
		result.write(output)
	input_file.close()
	result.close()

def count_fair_square(start, stop):
	return sum([square_palindrome(i) for i in xrange(start, stop+1)])

def square_palindrome(i):
	str_i = str(i)
	if str_i[-1] not in '14569':
		return 0
	elif len(str_i) in [2,4,8,10,14,18,20,24,30,38,40]:
		return 0
	elif palindrome(str_i):
		square_res = is_square(i)
		if square_res[0] and palindrome(square_res[1]):
			return 1
	return 0

def palindrome(i):
	"""(str) -> bool
	>>>palindrome('3')
	True
	>>>palindrome('151')
	True
	"""
	l = len(i)
	if l == 1:
		return True
	half = l//2
	for n in range(half):
		if i[n] != i[-1-n]:
			return False
	return True

def is_square(integer):
	root = math.sqrt(integer)
	if int(root + 0.5) ** 2 == integer: 
		return (True, str(root)[:-2])
	else:
		return (False, str(root)[:-2])

find_fair_square('C-small-attempt0.in')