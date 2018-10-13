import sys
import math


handle = open(sys.argv[1])
f = open('output1.txt','w')
lines = handle.readlines()
t_no = int(lines[0].strip())  #No of test cases
for t_no in range(1,t_no+1):
	s_i = ((t_no - 1) * 10) + 1
	e_i = ((t_no - 1) * 10) + 11
	if t_no == 1:
		s_i = 1
	case_lines = lines[s_i:e_i]
	row_1 = int(case_lines[0].strip())
	pat_1 = case_lines[1:5]
	row_2 = int(case_lines[5].strip())
	pat_2 = case_lines[6:]
	l_1 = pat_1[row_1-1].strip().split()
	l_2 = pat_2[row_2-1].strip().split()
	comm = list(set(l_1) & set(l_2))
	if len(comm) == 1:
		f.write("Case #" + str(t_no) + ": " + comm[0] + "\n")
	elif len(comm) == 0:
		f.write("Case #" + str(t_no) + ": " + "Volunteer cheated!" + "\n")
	elif len(comm) > 1:
		f.write("Case #" + str(t_no) + ": " + "Bad magician!" + "\n")

f.close()

handle.close()
