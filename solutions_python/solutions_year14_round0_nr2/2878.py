
out_file = open('b_out.txt', 'w')

def out(case_idx, num):
	print("Case #%d: %.7f" % (case_idx + 1, num), file=out_file)

def get_time(target, rate):
	return target / rate

with open('B-large.in') as f:
	num_cases = int(f.readline())
	for i in range(num_cases):
		[cost, increase, target] = [float(x) for x in f.readline().split(" ")]

		cur_rate = 2
		best_time = get_time(target, cur_rate)
		time_to_add = 0.0
		while True:
			time_to_add += get_time(cost, cur_rate)
			cur_rate += increase
			alt_time = get_time(target, cur_rate) + time_to_add

			if alt_time < best_time:
				best_time = alt_time
			else:
				break

		alt_time = get_time(target, 2 + increase) + cost

		out(i, best_time)

		

