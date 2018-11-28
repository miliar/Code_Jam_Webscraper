import math

def is_palindrome(num):
	return str(num)[::-1] == str(num)

def fair_and_square(lower_bound, upper_bound):
	result = 0
	for num in xrange(lower_bound, upper_bound+1):
		if is_palindrome(num) and math.sqrt(num) % 1 == 0 and is_palindrome(int(math.sqrt(num))):
			result += 1
	return result

f = open('C-small-attempt0.in', 'r')
file_content = f.readlines()[1:]

f = open('C-small.out', 'a')

for num, line in enumerate(file_content):
	lower_bound, upper_bound = int(line.split(' ')[0]), int(line.split(' ')[1])
	f.write('Case #%d: %d\n' % (num+1, fair_and_square(lower_bound, upper_bound)))

f.close()
