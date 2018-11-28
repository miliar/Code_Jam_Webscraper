import numpy as np
import scipy as sp
import pdb
import sys


def run_for_test_case(f   ):

	output_string = ""

	vals = f.readline().strip().split()
	C = float(vals[0])
	F = float(vals[1])	
	X = float(vals[2])
	r = 2.0

	t = 0

	while True:
		
		t_x = X / r
		t_c = C / r + X / (r+F)

		if t_x > t_c:
			t += C/r	
			r += F
		else:
			t += t_x
			break


	output_string = "%.7f" % t
		
	return output_string


if __name__ == "__main__":

	f = open (sys.argv[1], "r")
	fo = open (sys.argv[2],"w")
	
	vals = f.readline().strip().split()
	num_test_cases = int(vals[0])
	
#	# other values
#	vals = f.readline().strip().split()
#	v1 = int(vals[0])
#	v2 = int(vals[1])
	
	for i in xrange(num_test_cases):
		
		output_string = run_for_test_case(f  )
		fo.write( "Case #"+str(i+1)+": " + output_string + "\n")

