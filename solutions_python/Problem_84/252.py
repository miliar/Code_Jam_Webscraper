import os
import sys
import math

input_file_name = "A-large.in"

def replace(my_map, row, col):
	if((row == current_params[0]-1) or (col == current_params[1]-1)):
		return False
	if(my_map[row+1][col] != "#" or my_map[row+1][col+1] != "#" or my_map[row][col+1] != "#" ):
		return False
	else:
		my_map[row][col] = "/"
		my_map[row][col+1] = "\\"
		my_map[row+1][col] = "\\"
		my_map[row+1][col+1] = "/"
		return True

if __name__ == "__main__":
	in_handle = open(input_file_name, "r")
	testcase = int(in_handle.readline())
	test_case_counter = 1
	while test_case_counter < testcase + 1 :
		current_params = map(int, in_handle.readline().split())
		my_map=[]
		scounter =0 
		while scounter < current_params[0]:
			my_row = list(in_handle.readline().strip())
			my_map.append(my_row)
			scounter += 1
		#print my_map
		impossible = False
		for fcounter in range(0, current_params[0]):
			for scounter in range(0, current_params[1]):
				#print fcounter, scounter
				if(my_map[fcounter][scounter] == '#'):
					if not replace(my_map, fcounter, scounter):
						impossible = True;
						break;
			if impossible:
				#print impossible
				break;
		#print my_map
		print "Case #%d:" %(test_case_counter)
		if impossible:
			print "Impossible"
			
		else:
			for fcounter in range(0, current_params[0]):
				print "".join(my_map[fcounter])
		test_case_counter +=1