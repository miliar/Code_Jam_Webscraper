import sys
import math

data = [map(float, line.strip().split()) for line in sys.stdin.readlines()]

cases = data[0][0]
values = data[1:]

def solve_case(c, f, x):
	nf = 0
	t = 0
	previous_ttw = float("inf")
	ttw = float("inf")
	while not (previous_ttw < ttw):
		previous_ttw = ttw
		current_rate = nf * f + 2
		ttw = t + x / current_rate
		t += c / current_rate
#		print nf, t, current_rate, ttw, previous_ttw
		nf += 1
	return previous_ttw

for case in range(int(cases)):
	case_values = values[case]
	print "Case #%d: %s" % (case+1, solve_case(*case_values))
	