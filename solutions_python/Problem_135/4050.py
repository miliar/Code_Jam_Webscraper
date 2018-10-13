lines = open('A-small-attempt0.in').read().splitlines()

num_tests = int(lines[0])

start_index = 0
for curr_test in range(1, num_tests + 1):
	vol_ans = int(lines[start_index + 1])
	arr1 = map(int, lines[start_index + 1 + vol_ans].split(' ' , 4))
	vol_ans2 = int(lines[start_index + 1 + 4 + 1])
	arr2 = map(int, lines[start_index + 1 + 4 + 1 + vol_ans2].split(' ' , 4))
	possible_ans = list(set(arr1) & set(arr2))
	if len(possible_ans) == 1:
		print("Case #{}: {}".format(curr_test, possible_ans[0]))
	elif len(possible_ans) == 0:
		print("Case #{}: Volunteer cheated!".format(curr_test))
	else:
		print("Case #{}: Bad magician!".format(curr_test))

	start_index = start_index + 10