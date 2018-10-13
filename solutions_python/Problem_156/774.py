import math
def solve_recursive(count_array):
	if max(count_array.keys()) == 1:
		return 1
	else:
		max_pancakes = max(count_array.keys())
		max_pancakes_num_dinners = count_array[max_pancakes]
		del count_array[max_pancakes]
		half_max = int(max_pancakes/2)
		current_minimum = max_pancakes
		for j in range(half_max):
			arr_copy = count_array.copy()
			if arr_copy.has_key(j + 1):
				arr_copy[j + 1] += max_pancakes_num_dinners
			else:
				arr_copy[j + 1] = max_pancakes_num_dinners
			val_2 = max_pancakes - j - 1
			if arr_copy.has_key(val_2):
				arr_copy[val_2] += max_pancakes_num_dinners
			else:
				arr_copy[val_2] = max_pancakes_num_dinners
			result = solve_recursive(arr_copy) + max_pancakes_num_dinners
			if result < current_minimum:
				current_minimum = result
			del arr_copy
		return current_minimum

f_in = open("c:/In/B-small-attempt2.in",'r')
f_out = open("c:/In/B-small-attempt2.out",'w')
nlines = int(f_in.readline())
for i in range(nlines):
	dinners_count = int(f_in.readline())
	dinners_pancakes = f_in.readline().split()
	dinners_pancakes = map(lambda x: int(x),dinners_pancakes)
	pancakes_counter = dict()
	for j in range(len(dinners_pancakes)):
		if(pancakes_counter.has_key(dinners_pancakes[j])):
			pancakes_counter[dinners_pancakes[j]] += 1
		else:
			pancakes_counter[dinners_pancakes[j]] = 1
	# here count array is ready and sorted
	computed_res = solve_recursive(pancakes_counter)
	f_out.write("Case #" + str(i + 1) + ": " + str(computed_res) + "\n")
	print dinners_pancakes
	print "Case #" + str(i + 1) + ": " + str(computed_res) + "\n"
	del pancakes_counter
f_in.close()
f_out.close()