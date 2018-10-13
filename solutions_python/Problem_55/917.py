#!/usr/bin/env python
import sys
file = open(sys.argv[1],'r')
num_test_cases = file.readline()
num_test_cases = num_test_cases.rstrip("\n")
for i in range(0, int(num_test_cases)):
	run_capacity_groups = file.readline()
	run_capacity_groups = run_capacity_groups.rstrip("\n")
	rcg = run_capacity_groups.split(" ")
	groups = file.readline()
	groups=groups.rstrip("\n")
	groups_array = groups.split(" ")
	temp_arr = groups_array
	euros = 0
	for j in range(0,int(rcg[0])):
		sum = 0
		arr = []
		arr1 = []
		index = 0
		for elem in temp_arr:
			if sum+int(elem) <=int(rcg[1]):
				sum = sum+int(elem)
				euros = euros+int(elem)
				arr.append(int(elem))
				index +=1
			else:
				break
		#print arr
		arr1 = temp_arr[index:len(temp_arr)]
		for elem in arr:
			arr1.append(elem)
		temp_arr = arr1
		#print arr1
	print "Case #"+str(i+1)+": "+ str(euros)

