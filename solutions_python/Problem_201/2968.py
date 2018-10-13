# Written by Juliana Zhu
# For Google Code Jam 2017
# Problem B - Simple Case
# 8 April 2017 Sydney time

def solve(n_stalls, n_people):
	global_max_contiguous_empty = [n_stalls]
	max_empty = None
	min_empty = None
	for person in range(0, n_people):
		# print("Person #{} walking in.".format(person))
		max_contiguous_empty = global_max_contiguous_empty.pop(0)
		# print("Max contiguous empty = ", max_contiguous_empty)
		if max_contiguous_empty % 2:		# odd
			max_empty = min_empty = max_contiguous_empty // 2
		else: 								# even
			max_empty = max_contiguous_empty // 2
			min_empty = max_empty - 1
			if min_empty < 0:
				min_empty = 0
		global_max_contiguous_empty.append(max_empty)
		global_max_contiguous_empty.append(min_empty)
		global_max_contiguous_empty = sorted(global_max_contiguous_empty, reverse=True)
		# print("Global Max Contiguous Empty", global_max_contiguous_empty)
	return max_empty, min_empty


filename = "C-small-1-attempt2"
f = open(filename + ".in")
line = f.readline()
problems = [None] * int(line)
i = 0
while line:
	line = f.readline()
	if not line:
		break
	n_stalls, n_people = line.split(' ')
	n_stalls = int(n_stalls.strip())
	n_people = int(n_people.strip())
	problems[i] = [n_stalls, n_people]
	i += 1
f.close()

# for j, problem in enumerate(problems):
# 	min_empty, max_empty = solve(problem[0], problem[1])
# 	print("Case #{}: {} {}".format(j + 1, min_empty, max_empty))

target = open(filename + ".out", 'w')
for j, problem in enumerate(problems):
	min_empty, max_empty = solve(problem[0], problem[1])
	target.write("Case #{}: {} {}\n".format(j + 1, min_empty, max_empty))
target.close()