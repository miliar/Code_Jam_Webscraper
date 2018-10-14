#!/usr/bin/python


import sys

f = open(sys.argv[1], 'r')


line_num = 0;
case = 1
for line in f:
	if line_num == 0:
		num_of_lines=int(line[:-1])
		line_num+=1
		continue 
	number_stood = 0
	number_invited = 0
	max_shy = int(line[0])
	shy_freq=line[2:]
	for shyness in range(0,max_shy):
		number_stood+=int(shy_freq[shyness])
		while number_stood < shyness+1:
			number_invited+=1
			number_stood+=1
	out_string = "Case #" + str(case) + ": " + str(number_invited)
	print out_string
	case+=1

