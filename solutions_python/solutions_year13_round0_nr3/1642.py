#!/usr/bin/python
import fileinput
#import time

line_number = 0
#f = 'sample_input.txt'
#f = 'C-small-attempt0.in'
f = 'C-large-1.in'


def int_sqrt(x):
	if x < 0:
		raise ValueError('square root not defined for negative numbers')
	n = int(x)
	if n == 0:
		return 0
	a, b = divmod(n.bit_length(), 2)
	x = 2**(a+b)
	while True:
		y = (x + n//x)//2
		if y >= x:
			return x
		x = y

def is_palindrome(n):
	if (n - int(str(n)[::-1])) == 0:
		return True
	else:
		return False

def pre_compute(upper_range):
	upper_bound_sqrt = int_sqrt(upper_range)
	f_n_sq_list = []
	i = 1
	while i <= (upper_bound_sqrt + 1):
		if (is_palindrome(i)):
			#go further to test if its square is a palindrome only if it is already a palindrome
			i_sq = i**2
			if (is_palindrome(i_sq) and i_sq <= upper_range):
				f_n_sq_list.append(i_sq)
				#fair_and_square_count += 1
		i += 1
	
	return f_n_sq_list	
	

f_n_sq_list = pre_compute(10**14)

for line in open (f, 'r'):
        if line_number == 0:
                #this is the number of test case
                test_case_count = int(line)
        elif (line_number) <= test_case_count:
		#get range
		lower_bound, upper_bound = line.strip().split(' ')
		lower_bound = int(lower_bound)
		upper_bound = int(upper_bound)
		lower_bound_sqrt = int_sqrt(lower_bound)
		upper_bound_sqrt = int_sqrt(upper_bound)

		#print lower_bound_sqrt, upper_bound_sqrt

		fair_and_square_count = 0

		
		for f_n_sq_num in f_n_sq_list:
			if (f_n_sq_num >= lower_bound and f_n_sq_num <= upper_bound):
				fair_and_square_count += 1 
		
		
		print "Case #"+str(line_number)+": "+str(fair_and_square_count)
        line_number = line_number + 1



