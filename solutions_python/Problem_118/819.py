#!/bin/python
from math import ceil, log, sqrt
t = int(raw_input().strip())
for case in range(t):
	lower, upper = [int(bound.strip()) for bound in raw_input().strip().split()]
	
	fingers = 10
	lower_digit_bound = len(str(int(sqrt(lower))))
	upper_digit_bound = len(str(int(sqrt(upper)))) + 1 # Inclusive range

	total = 0
	for digits in xrange(lower_digit_bound, upper_digit_bound):
		# Generate palindromes with (digits) digits.
		number_of_unique_digits = max(int(ceil(digits/2.0)), 1)
		for trial in xrange(int(fingers**(number_of_unique_digits - 1)), int(fingers**number_of_unique_digits)):
			palindrome = str(trial)
			palindrome = int(palindrome + palindrome[:digits - len(palindrome)][::-1])
			assert len(str(palindrome)) == digits
			palindrome_squared = palindrome ** 2
			if str(palindrome_squared) == str(palindrome_squared)[::-1] and lower <= palindrome_squared and upper >= palindrome_squared:
				total += 1
	print "Case #{0}: {1}".format(case + 1, total)
				
