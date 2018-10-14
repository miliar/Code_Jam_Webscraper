import os
import sys



input_file_name = "C-small-attempt1.in"

in_handle = open(input_file_name, "r")
testcase = int(in_handle.readline())
test_case_counter = 1
while test_case_counter < testcase + 1 :
	current_params = map(int, in_handle.readline().split())
	symph = map(int, in_handle.readline().split())
	done =True
	for num in range(current_params[1], current_params[2]+1):
		done = True;
		for i in symph:
			if i < num :
				if num%i != 0:
					done=False;
					break
			else:
				if i%num !=0 :
					done = False;
					break;
		if done:
			print "Case #%d: %d"%(test_case_counter, num)
			break;
	if not done:
		print "Case #%d: NO"%(test_case_counter)
		
	test_case_counter +=1
				
						