from math import sqrt
file_name = 'C-small-attempt0'
input_file_name = file_name + '.in'
output_file_name = file_name + '.out'

def is_palindrome(i):
	return i == int(str(i)[::-1])

def is_square(i):
	r = int(sqrt(i))
	if i != r*r:
		return False
	return is_palindrome(r)

with open(input_file_name) as input_file, open(output_file_name, 'w') as output_file:
	N = int(input_file.readline())
	for T in xrange(N):
		line = input_file.readline()
		A, B = map(int, line.split(' '))
		s = 0
		for i in xrange(A, B+1):
			if is_palindrome(i) and is_square(i):
				s += 1
		output_file.write('Case #{T}: {s}\n'.format(T=T+1, s=s))

