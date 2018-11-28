def epilogue(result, num):
	out_file.write("Case #" + str(num+1) + ": " + result + '\n')

in_file, out_file = open('B-large.in', 'r'), open('B-large.out', 'w')

def valid(indices, P):
	for index in indices:
		if index >= P:
			return False
	return True

num_cases = int(in_file.readline())
for case_num in range(num_cases):
	N, P = [int(x) for x in in_file.readline().split()]
	R = [int(x) for x in in_file.readline().split()]
	Q = [sorted([int(x) for x in in_file.readline().split()]) for _ in range(N)]
	for i in range(len(Q)):
		Q[i].reverse()

	indices = [0 for _ in range(N)]
	num_kits = 0
	while valid(indices, P):
		curr_values = [Q[i][indices[i]] for i in range(N)]
		ratio = [curr_values[i] / R[i] for i in range(N)]

		succeeded = False
		for num_servings in range(int(min(ratio)), int(max(ratio)) + 2):
			can_make = True
			for i in range(len(curr_values)):
				value = curr_values[i]
				lower_bound, upper_bound = 0.9*num_servings*R[i], 1.1*num_servings*R[i]
				if lower_bound <= value and value <= upper_bound:
					continue
				else:
					can_make = False
					break

			if can_make:
				for i in range(len(indices)):
					indices[i] += 1
				num_kits += 1
				succeeded = True
				break
		if not succeeded:
			indices[ratio.index(max(ratio))] += 1
	epilogue(str(num_kits), case_num)
