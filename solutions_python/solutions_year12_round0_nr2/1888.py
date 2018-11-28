#!C:\Python27.python.exe -u

print "Google code jam 2012 - Qualification round - Problem B"

# Import the required modules
# Initialization
import sys
sys.path.append("C:\\Users\\vyaram\\Desktop\\code_jam\\Utilities")

import my_utilities

import os
import string
import bisect



# Open the I/O files
# Input file descriptor
fd_in = open("input_file.in", 'r')

# Output file descriptor
fd_out = open("output_file.in", 'w')

# Get the number of test cases
total_num_of_test_cases = my_utilities.get_number_of_test_cases(fd_in)
print "Number of test cases = ", total_num_of_test_cases


test_case_num = 1
while test_case_num <= total_num_of_test_cases:
    # To read a line from the input file
    raw_str = fd_in.readline()
    tmp_list = raw_str.split()
    b = int(tmp_list[2])
    s = int(tmp_list[1])
    out = 0
    print "N = ", tmp_list[0]
    print "S = ", tmp_list[1]
    print "b = ", tmp_list[2]
    score_int_list = map(int, tmp_list[3:3+int(tmp_list[0])])
    score_int_list.sort(reverse=True)
    print score_int_list

    for i in range(len(score_int_list)):
        print score_int_list[i], i

        x = score_int_list[i]
        z = x - (2*b)

        if x < b:
            break

        if z >= (b-2):
            out = out +1
            print " x = " , x
        elif ((z == (b-3)) or (z == (b-4))) and (s >= 1):
            out = out + 1
            s = s -1
        else:
            break
        
        
    print "out = ", out
    print "s = " , s

    my_utilities.print_test_case_output(fd_out, test_case_num, str(out))




    test_case_num = test_case_num + 1
    print "\n"

    



# To write a line to the output file
# fd_out.write(out_str)






# Close the opened files
fd_in.close()
fd_out.close()
