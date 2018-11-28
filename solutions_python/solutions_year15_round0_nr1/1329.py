number_cases = int(raw_input())

def solve(vals):
	missing = 0
	current_sum = 0
	for ind, val in enumerate(vals):
		if current_sum < ind:
			missing += ind - current_sum
			current_sum = ind
		current_sum += val
	return missing

for i in xrange(number_cases):
	max_s, ss = raw_input().split()
	vals = [int(x) for x in ss]
	print "Case #{}: {}".format(i+1, solve(vals))