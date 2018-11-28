#!/usr/bin/python
#This program requires python ver 2.6 or higher. (itertools.combinations)
import sys
import itertools

#solve case function
def solve_case(n, d, g, case_number):
	is_possible = False;
	if (int(g) == 100 and int(d) != 100) or (int(g) == 0 and int(d) != 0):
		is_possible = False
	elif int(d) == 0:
		is_possible = True
	elif int(n) < minlist[int(d) - 1]: 
		is_possible = False 
	else:
		is_possible = True 

	if is_possible:
		print "Case #" + str(case_number) +": Possible"
	else:
		print "Case #" + str(case_number) +": Broken"

#main
r = sys.stdin

if len(sys.argv) > 1:
	r = open(sys.argv[1], 'r')

minlist = []
for i in range(1, 101):
	for j in range(1, 101):
		p = j * float(i) / 100
		if p == int(p):
			minlist.append(j)
			break

total_cases = r.readline()
for case_number in range(1, int(total_cases) + 1):
	fsta = r.readline().strip().split(' ')
	solve_case(fsta[0], fsta[1], fsta[2], case_number)

