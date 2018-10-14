from sys import stdin
import math
import itertools

def palindrome(digits):
	r = len(digits) - 1
	l = 0
	while l < r and digits[l] == 0:
		l += 1
	while l < r:
		if digits[l] != digits[r]:
			return False
		l += 1
		r -= 1
	return True

def length(n):
	l = 0
	while n > 0:
		l += 1
		n /= 10
	return l

def to_number(digits):
	n = 0
	for d in digits:
		n = n * 10 + d
	return n

def to_digits(n):
	digits = []
	while n > 0:
		digits.append(n % 10)
		n /= 10
	return digits

def make_palindrome(half, even):
	half = list(half)
	full = half[::]
	if even:
		left = reversed(half)
	else:
		left = reversed(half[:-1])
	for x in left:
		full.append(x)
	return full

def good_palindromes(length):
	if length == 1:
		yield [1]; yield [2]; yield [3]
		return
	even = length % 2 == 0
	n = (length + 1) / 2
	
	for d in itertools.product(range(2), repeat = n - 1):
		yield make_palindrome([1] + list(d), even)

	yield make_palindrome([2] + [0] * (n - 1), even)
	if not even:
	 	yield make_palindrome([2] + [0] * (n - 2) + [1], even)

	 	for i in xrange(n - 2):
	 		b = [0] * (n - 2)
	 		b[i] = 1
	 		yield make_palindrome([1] + b + [2], even)

def solve(A, B):
	a = (length(A) + 1) / 2
	b = (length(B) + 1) / 2
	answer = 0
	for n in xrange(a, b + 1):
		for digits in good_palindromes(n):
			x = to_number(digits)
			s = x * x
			if s < A or s > B:
				continue
			#print x, s
			answer += 1
	return answer

T = int(stdin.readline())
for t in xrange(T):
	A, B = map(int, stdin.readline().split())
	answer = solve(A, B)
	print 'Case #%d:' % (t + 1), answer