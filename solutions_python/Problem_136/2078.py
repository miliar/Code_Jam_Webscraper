def do_i_need_a_farm(cps, c, f, goal):
	time_without_farm = goal / cps

	time_till_farm = c / cps
	time_with_farm = goal / (cps + f)

	return time_without_farm > (time_till_farm + time_with_farm)


def solve(c, f, x):
	# c - cost of farm
	# f - farm's cps 
	# x - goal

	current_cps = 2
	result = 0
	while (do_i_need_a_farm(current_cps, c, f, x)):
		result += c / current_cps
		current_cps += f
	result += x / current_cps
	return result


with open("B-small-attempt0.out.txt", "w") as fr:
	with open("B-small-attempt0.in.txt", "r") as f:
		test_cases = int(f.readline())
		for test_num in xrange(test_cases):
			cfx = map(float, f.readline().split(" "))
			fr.write("Case #%s: %.7f\n" % (test_num + 1, solve(*cfx)))

