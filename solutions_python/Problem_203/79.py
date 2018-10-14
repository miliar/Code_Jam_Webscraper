def epilogue(result, num):
	out_file.write("Case #" + str(num+1) + ": " + result + '\n')

in_file, out_file = open('A-large.in', 'r'), open('A-large.out', 'w')

num_cases = int(in_file.readline())
for case_num in range(num_cases):
	R, C = [int(x) for x in in_file.readline().split()]
	cake = [list(in_file.readline().rstrip()) for _ in range(R)]

	# Pass 1
	for i in range(len(cake)):
		setter = None
		first_idx = None
		first_setter = None
		for j in range(len(cake[i])):
			c = cake[i][j]
			if c != '?':
				if first_idx is None:
					first_idx = j
					first_setter = c
				setter = c
			else:
				cake[i][j] = setter
		if first_idx is not None:
			for j in range(first_idx):
				cake[i][j] = first_setter

	# Pass 2 - should only have rows of fully None values
	first_non_none = None
	last_non_none = None
	for i in range(len(cake)):
		if cake[i][0] != None:
			first_non_none = i
			break

	for i in range(len(cake)-1, -1, -1):
		if cake[i][0] != None:
			last_non_none = i
			break
	
	if first_non_none != 0:
		for i in range(first_non_none):
			for j in range(len(cake[i])):
				cake[i][j] = cake[first_non_none][j]

	if last_non_none != len(cake) - 1:
		for i in range(last_non_none+1, len(cake)):
			for j in range(len(cake[i])):
				cake[i][j] = cake[last_non_none][j]

	for i in range(first_non_none+1, last_non_none):
		if cake[i][0] is None:
			for j in range(len(cake[i])):
				cake[i][j] = cake[i-1][j]
		else:
			continue

	out_file.write("Case #" + str(case_num+1) + ":\n")
	for i in range(len(cake)):
		row = "".join(cake[i])
		row = row + "\n"
		out_file.write(row)





