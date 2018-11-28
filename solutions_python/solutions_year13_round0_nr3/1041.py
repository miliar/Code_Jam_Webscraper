import numpy as np
import scipy as sp
import pdb


def is_palindrome(s):

	for i in xrange(len(s)/2):
		if not s[i] == s[-i-1]:
			return False
	return True

def run_for_test_case(f   ):


	range_vals = f.readline().strip().split()
	range_vals = (int(range_vals[0]), int(range_vals[1]))
	
	sqrt_range_vals = (int(np.ceil(range_vals[0]**0.5)), int(np.floor(range_vals[1]**0.5)))

	counter = 0
	for number in xrange(sqrt_range_vals[0], sqrt_range_vals[1]+1):
		
		square_num = number**2
		if is_palindrome(str(number)) and is_palindrome(str(square_num)):
			counter += 1
			#print "Found: ", number, square_num

	output_string = str(counter)
	#print "--------------"
	return output_string


if __name__ == "__main__":

	f = open ("C-small-attempt0.in", "r")
	fo = open ("C-small-attempt0.out","w")
	
	vals = f.readline().strip().split()
	num_test_cases = int(vals[0])
	

	
	for i in xrange(num_test_cases):
		
		output_string = run_for_test_case(f  )
		fo.write( "Case #"+str(i+1)+": " + output_string + "\n")

