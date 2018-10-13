#!/usr/bin/python
#This program requires python ver 2.6 or higher. (itertools.combinations)
import sys
import itertools

#solve case function
def solve_case(N, L, H, notes, case_number):

	is_impossible = True 
	for n in range(L, H + 1):
		is_good = True
		for on in notes:
			if on % n != 0 and n % on != 0:
				is_good = False
				break
		else:
			if is_good:
				is_impossible = False 
				break
	
	if is_impossible:
		print "Case #" + str(case_number) + ": NO"
	else:
		print "Case #" + str(case_number) + ": " + str(n)

#main
r = sys.stdin

if len(sys.argv) > 1:
	r = open(sys.argv[1], 'r')

total_cases = r.readline()
for case_number in range(1, int(total_cases) + 1):
	N_L_H = r.readline().strip().split(' ')
	notes = r.readline().strip().split(' ')
	solve_case(int(N_L_H[0]), int(N_L_H[1]), int(N_L_H[2]), map(int, notes), case_number)

