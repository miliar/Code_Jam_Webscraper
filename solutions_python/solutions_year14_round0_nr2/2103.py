import sys

def solve_problem(test_no):
	(farm_cost, farm_earn, target) = [float(i) for i in raw_input().split()]

	substitutions = []
	farm_time = 0.0
	farm_no = 0
	former_value = sys.float_info.max
	per_earn = 2.0
	while True:
		current_value = farm_time + (target / per_earn)
		if current_value > former_value: break
		former_value = current_value
		substitutions.append(current_value)
		farm_time += farm_cost / per_earn
		farm_no += 1
		per_earn = 2.0 + farm_earn * farm_no

	result = 0.0
	if len(substitutions) == 0:
		result = target / per_earn
	else:
		result = min(substitutions)

	print "Case #%d: %.7f" % (test_no, result)

test_cases = int(raw_input())
for i in xrange(test_cases):
	solve_problem(i+1)