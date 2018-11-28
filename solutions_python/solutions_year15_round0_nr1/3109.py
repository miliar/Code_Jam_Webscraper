#!/usr/local/bin/python
import numpy as np
import math


# path = "A-small-attempt2.in"
path = "A-large.in"
out_path = "R1-A_Large.txt"
f_in = open(path)
T = int(f_in.readline())

f_out = open(out_path, 'w')

case_counter = 0;

while(case_counter <T):
	line = f_in.readline()
	s_line = line.split()
	max = int(s_line[0])
	aud = s_line[1]
	aud_size = len(aud)
	running_total = 0
	mem_to_add = 0
	for i in range(0,aud_size-1):
		running_total += int(aud[i])
		if running_total<(i+1):
			mem_to_add+=(i+1-running_total)
			running_total+=(i+1-running_total)
		if running_total>max:
			break
	f_out.write('Case #'+str(case_counter+1)+': '+str(mem_to_add)+'\n')
	case_counter+=1

