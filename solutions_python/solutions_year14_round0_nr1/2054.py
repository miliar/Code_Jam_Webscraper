import numpy as np
import scipy as sp
import pdb
import sys


def run_for_test_case(f   ):

	a1 = int(f.readline())
	mat = np.zeros((4,4))

	for i in xrange(4):
		mat[i,:] = [int(x) for x in f.readline().strip().split()]


	subset1 = set(mat[a1-1,:])
	a2 = int(f.readline())

	for i in xrange(4):
		mat[i,:] = [int(x) for x in f.readline().strip().split()]

	subset2 = set(mat[a2-1,:])

	result = subset1.intersection(subset2)

	output_string = ""

	if len(result) == 0:
		output_string = "Volunteer cheated!"
	elif len(result) == 1:
		output_string = str(int(list(result)[0]))
	else:
		output_string = "Bad magician!"
	

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

