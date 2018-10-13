#!/usr/bin/python
import sys, string, math

#solve case function
def solve_case(min, max, case_number):
	ans = 0
	max_str = str(max)
	digit_range = range(1, len(str(max)))
	for candidate in range(min, max):
		candidate_str = str(candidate)
		for rot_candidate in set([candidate_str[rot:] + candidate_str[:rot] for rot in digit_range]):
			if rot_candidate <= max_str and candidate_str < rot_candidate:
				ans = ans + 1

	print "Case #%d: %d" % (case_number, ans)

#main
r = sys.stdin

if len(sys.argv) > 1:
	r = open(sys.argv[1], 'r')

total_cases = r.readline()
for case_number in range(1, int(total_cases) + 1):
	case = map(int, r.readline().rstrip().split(' '))
	solve_case(case[0], case[1], case_number)

