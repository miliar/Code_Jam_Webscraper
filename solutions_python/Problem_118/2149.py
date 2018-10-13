import math

def is_palindrome(n):
	s = str(n)
	return s == s[::-1]

def nb_fair_squares(A, B):
	n = 0

	i = int(math.ceil(math.sqrt(A)))
	while i ** 2 <= B:
		if is_palindrome(i) and is_palindrome(i ** 2):
			n += 1
		i += 1

	return n

T = int(raw_input())
for x in xrange(1, T + 1):
	[A, B] = map(int, raw_input().split(' '))
	y = nb_fair_squares(A, B)
	print('Case #%d: %d' % (x, y))
