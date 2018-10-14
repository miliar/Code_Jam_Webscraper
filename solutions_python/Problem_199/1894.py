def solve(inpt, size): 
	count = 0 
	for i in range(len(inpt)-size+1): 
		if inpt[i] == -1: 
			count += 1
			for j in range(i, i+size):
				inpt[j] *= -1 

	for i in range(len(inpt)): 
		if inpt[i] == -1: 
			return "IMPOSSIBLE"

	return count

num_lines = int(raw_input())
for i in range(num_lines): 
	test_case = raw_input()
	[config, size] = test_case.split(" ")
	size = int(size)

	data = [] 
	for p in config: 
		if p == '+': 
			data.append(1) 
		elif p == '-': 
			data.append(-1)

	answer = solve(data, size)
	print "Case #%d: %s" % (i+1, answer)


