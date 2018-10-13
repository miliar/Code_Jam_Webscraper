import os
import sys
import math
import operator


if __name__=="__main__":
	in_handle = open('C-large.in', "r")
	test_case_count  = int(in_handle.readline())
	test_case_counter = 1;
	while(test_case_counter < test_case_count +1 ):
		numbers = int(in_handle.readline())
		number_list = map(int, in_handle.readline().split())
		if(reduce(operator.xor, number_list) != 0):
			print "Case #%d: NO" %(test_case_counter)
		else:
			print "Case #%d: %d" %(test_case_counter, (sum(number_list) - min(number_list)))
		test_case_counter = test_case_counter+1