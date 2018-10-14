import sys
import os

ifd = open("small.in", "r")
ofd = open("out.txt", "w")  
no_of_testcase = int(ifd.readline())
item_map = {} 
for i in range(no_of_testcase) :
    testcase_detail_str = ifd.readline() ; 
    testcase_detail_arr = testcase_detail_str.split() 
    value_of_A = int(testcase_detail_arr[0]) 
    value_of_B = int(testcase_detail_arr[1])
    value_of_K = int(testcase_detail_arr[2])
    value_of_result = 0  
    for a in range(value_of_A) :
        for b in range(value_of_B) : 
            and_result = a & b
            if(and_result < value_of_K) : 
                 value_of_result = value_of_result + 1 
    ofd.write("Case #"+ str(i+1) + ": " + str(value_of_result) + "\n")
ifd.close()
ofd.close()


