n_cases = int(raw_input())

def read_int():
	return int(raw_input())

def read_arrangement():
	return [eval("[ " + raw_input().replace(" ", ",") + " ]") for i in range(4)]

def transpose_arrangement(arr):
	return [[ x[i] for x in arr] for i in range(4)]

for case in range(1, n_cases+1):
	answer1 = read_int() - 1
	arrange1 = read_arrangement()
	answer2 = read_int() - 1
	arrange2 = read_arrangement()
	
	row1_nums = set(arrange1[answer1])
	row2_nums = set(arrange2[answer2])

	#arrange2_t = transpose_arrangement(arrange2)
	#row2t_nums = set(arrange2_t[answer2])

	solutions = set.intersection(row1_nums, row2_nums)

	if len(solutions) == 1:
		output = list(solutions)[0]
	elif len(solutions) == 0:
		output = "Volunteer cheated!"
	else:
		output = "Bad magician!"

	print "Case #%d: %s" % (case, output)
