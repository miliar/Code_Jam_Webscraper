#!/usr/bin/env python

###### Modules ######
import os
import math
import string
import sys
#####################

##########################################################################
working_dir = "C:\Users\MyPC\Documents\codejam_2013\Lawnmover_Qual_2013\\"
input_file = "B-small-attempt2.in"
output_file = "B-small-attempt2.out"
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
    (N, M) = (in_file.readline()).split()
    N = int(N)
    M = int(M)
    Mat = []
    for count in range(N):
        A = (in_file.readline()).split()
        Mat.append(A)
    #print N
    #print  "***************"
    #print M
    #print "****************"
    #print Mat
    #sys.exit(1)
    return [N, M, Mat]
#****************************************************************
def bounds(C):
    """Swap x and y coordinates. """
    if C < 0:
        return 0
    else:
        return C
#***************************************************************
def Compute_Result(test_case):
    """ Grab a single testcase, perform computation and return the result."""
    N = test_case[0]
    M = test_case[1]
    Mat = test_case[2]
    Sum_row = range(N)
    Sum_col = range(M)
    result = "NO"
    for i in range(N):
        for j in range(M):
            Mat[i][j] = int(Mat[i][j])
    #print "*****************"
    #print "MAt"
    #print Mat
    #print "************************"
    for i in range(N):
        Sum_row[i] = sum(Mat[i][:])
        #Sum_row[i] = int(math.ceil(float(sum(Mat[i][:]))/M))
        #print "***********"
        #print "row=", str(i)
        #print Sum_row[i]
    for j in range(M):
        Sum_col[j] = 0
        for k in range(N):
            Sum_col[j]+= Mat[k][j]
        #Sum_col[j] = int(math.ceil(float(Sum_col[j])/N))
        #print "***********"
        #print "col = ", str(j)
        #print Sum_col[j]
    for i in range(N):
        for j in range(M):
            loop_tst = "pass"
            x = Mat[i][j]*M
            y = Mat[i][j]*N
            if (x<Sum_row[i])and(y<Sum_col[j]):
                loop_tst = "fail"
                #print "++++++++++++++++"
                #print "Mat", str(i), str(j), "= ", Mat[i][j]
                ##print "Sum_row", str(i), " = ", Sum_row[i]
                #print "Sum_col", str(j), "= ", Sum_col[j]
                #print "++++++++++++++++++++++++"
            if loop_tst == "fail":
                return result
            
    result = "YES"
    
    return result
        

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
        formatted_result = 'Case #' + str(case_index) + ': ' + result
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
    #print T
    #sys.exit(1)
    # dictionary to store result of computation. Key = testcase#
    results ={}
    for index in range(T):
        case_index = index + 1
        test_case = Get_One_Test_Case(f)
        #print test_case
        #print '*************************************'
        results[case_index] = Compute_Result(test_case)
    print "T = ", T
    abs_out_file_path = working_dir + output_file
    #sys.exit(1)
    Save_And_Display_Results(results, abs_out_file_path)
    f.close()

#***************************************************************
if __name__ == '__main__':
    main()
    