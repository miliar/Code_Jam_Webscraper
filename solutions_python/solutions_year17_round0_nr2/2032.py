def solve(data): 
	for i in range(len(data)-1, 0, -1): 
		if data[i-1] > data[i]: 
			data[i-1] -= 1 
			for j in range(i, len(data)): 
				data[j] = 9
	return data


num_cases = int(raw_input()) 
for n in range(num_cases): 
	data = map(int, list(raw_input())) 
	print "Case #%d: %d" % (n+1, int("".join(map(str, solve(data)) )))