#!/usr/bin/env python

###### Modules ######
import os
import math
import string
import sys
from itertools import *
from collections import OrderedDict
#####################

##########################################################################
working_dir = "C:\codejam\source\\"
#input_file = "B-small-attempt2-chk.in"
#output_file = "B-small-attempt2-chk.out"

#input_file = "A_tst.in"
#output_file = "A_tst.out"
input_file = "A-large-1.in"
output_file = "A-large-1.out"

##########################################################################

#***************************************************************
def Grab_Input_File(working_dir, input_file):
    """ Input: working directory and input file name.
        Output: open input file and return file object. """
    abs_in_file_path = working_dir + input_file
    try:
        f = open(abs_in_file_path, 'rU')
    except IOError:
        print "Error: File not found"
        return 0
    return f
#****************************************************************
def Get_One_Test_Case(in_file):
    """ Extract one test case from the input file and
        put it in appropriate data structure.
        Input: file object, Output: a data structure containing single test case."""
    A = (in_file.readline()).split()
    x, y = A[0].split('/')
    return [int(x), int(y)]
#****************************************************************
#***************************************************************
def Compute_Result(test_case):
    """ Grab a single testcase, perform computation and return the result."""
    x = test_case[0]
    y = test_case[1]
    count = 0
    delta = -1
    first_flag = True
    if x > y:
	    return (1, False)
    if x/y == 1 and x%y!=0 :
	    return (1, True)
    ok = True
    while x != 0:
	    if y%2 != 0:
		    ok = False
		    break
	    delta = x - y/2
	    if delta < 0:
		    if first_flag:
			    count += 1
	    else:
		    x = x - y/2
		    if first_flag:
			    first_flag = False
			    count += 1
	    y = y/2
	    if count > 40:
		    ok = False
		    break 
    return (count, ok)
    
#***************************************************************        



#***************************************************************
def Save_And_Display_Results(results, output_file):
    """ Save the results into a specified output file and
        display the results on the screen."""
    def Format_Result(case_index, result):
        """ Returns the result transformed into one big string with
            new lines inserted at appropriate places. This string
            can be directly written into a file and also printed
            directly to screen."""
        ### Code to transform result into one big string.
        formatted_result = 'Case #' + str(case_index) + ': ' + str(result)
        return formatted_result
    
    f = open(output_file, 'w')
    for case_index in sorted(results.keys()):
        formatted_result_to_screen = Format_Result(case_index, results[case_index])
        formatted_result_to_file = formatted_result_to_screen + '\n'
        f.write(formatted_result_to_file)
        print '***************************************'
        print formatted_result_to_screen
    print '***************************************'
    

#***************************************************************
def main():
    f = Grab_Input_File(working_dir, input_file)
    # Extract the number of test cases.
    T = int(f.readline())
    # dictionary to store result of computation. Key = testcase#
    results ={}
    for index in range(T):
        test_case = Get_One_Test_Case(f)
	print test_case
	res = Compute_Result(test_case)
	print res
	can_do = res[1]
	if can_do:
		result = str(res[0])
        else:
		result = "impossible"
        case_index = index+1
        results[case_index] = result
        
    print "T = ", T
    abs_out_file_path = working_dir + output_file
    Save_And_Display_Results(results, abs_out_file_path)
    f.close()

#***************************************************************
if __name__ == '__main__':
    main()
    
