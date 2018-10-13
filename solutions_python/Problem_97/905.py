T = int(input())
for t in range(T):
	line = input().split()
	length = len(line[0])
	A = int(line[0])
	B = int(line[1])
	result = 0

	# For every number in [A,B-1]
	for x in range(A, B):
		orig_num_list = list(str(x))
		cycled_num_list_list = []
		# Cycle `n'(in [1, length-1]) digits of number `x'
		for n in range(1, length):
			# `0' can't be the head digit
			if orig_num_list[-n] == '0':
				continue
			# cycle it 
			cycled_num_list = orig_num_list[:]
			cycled_num_list[0:0] = cycled_num_list[-n:]
			cycled_num_list[-n:] = []
			# check the bound 
			# make sure `n < m' and 
			# avoid duplicating
			if cycled_num_list>=list(line[0]) and cycled_num_list<=list(line[1]) and cycled_num_list>orig_num_list \
			and cycled_num_list not in cycled_num_list_list:
				cycled_num_list_list.append(cycled_num_list)
				result += 1
	print("Case #" + str(t+1) + ": " + str(result))
