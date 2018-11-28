def solve(pancakes, t=0):
	# print(t, pancakes)
	# print(pancakes, t)

	# if all([p <= 3 for p in pancakes]):
	# 	return t + 3

	max_val = max(pancakes)
	max_i = pancakes.index(max_val)

	if max_val <= 3:
		return t + max_val

	# after_split = pancakes[:]
	# after_split[max_i] = max_val // 2
	# after_split.append(max_val - after_split[max_i])

	splits = []
	# for n in range(2, int(max_val ** 0.5 + 1)):
	for n in range(2, int(max_val * 0.5 + 1)):
		after_split = pancakes[:]
		after_split[max_i] -= n
		after_split.append(n)

		splits.append(after_split)

	# min_split = solve(splits, t + 1)
	# if max_val > min_split:
	# 	return max_val
	
	# wait = [x - 1 for x in pancakes if x - 1 > 0]

	return min([t + max_val] + list(map(lambda x: solve(x, t + 1), splits)))

# def solve_greedy(pancakes):
# 	time_passed = 0
# 	while len(pancakes) > 0:
# 		max_val = max(pancakes)
# 		max_i = pancakes.index(max_val)

# 		after_split = pancakes[:]
# 		after_split[max_i] = max_val // 2
# 		after_split.append(max_val - after_split[max_i])

# 		if (max(after_split) + 1) < max_val:
# 			pancakes = after_split
# 		else:
# 			pancakes = [x - 1 for x in pancakes if x - 1 > 0]

# 		time_passed += 1

# 	return time_passed

input_file = open("B-small-attempt4.in")
output_file = open("out", "w")

T = int(input_file.readline().strip())
for t in range(T):
	# print(t)

	D = int(input_file.readline().strip())
	pancakes = list(map(int, input_file.readline().strip().split(" ")))

	# # print(pancakes)

	# output_file.write("Case #{0}: {1}\n".format(t + 1, time_passed))
	output_file.write("Case #{0}: {1}\n".format(t + 1, solve(pancakes)))
	# print("Case #{0}: {1}\n".format(t + 1, solve(pancakes)))
