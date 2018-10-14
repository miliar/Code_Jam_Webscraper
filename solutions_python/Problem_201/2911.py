input_file = open("input.txt" , "r")
output_file = open("output.txt" , "w")

no_test = int(input_file.readline())

for l in range(no_test):
	input_str = input_file.readline()
	input_str = map(int , input_str.split())

	stalls = []
	for i in range(input_str[0] + 2):
		stalls.append(0)

	stalls[0] = 1
	stalls[-1] = 1
	
	starts = []
	lengths = []
	last_index = 0

	for i in range(input_str[1]):
		for j in range(len(stalls)):
			if(stalls[j] == 1):
				if(j == len(stalls) - 1):
					break
				starts.append(j)
				k = j + 1
				while(stalls[k] == 0):
					k = k + 1
				len_empty = k - 1 - j	
				lengths.append(len_empty) 

		max_dis = max(lengths)
		index_val = lengths.index(max_dis)

		if(max_dis % 2 == 1):
			displace_val = max_dis / 2 + 1
		else:
			displace_val = max_dis / 2
		stalls[starts[index_val] + displace_val] = 1
		last_index = starts[index_val] + displace_val
		lengths = []
		starts = []
	
	print_list = []

	pre_index = last_index - 1
	check_val = stalls[pre_index]
	counter = 0	
	
	while(check_val == 0):
		counter = counter + 1
		pre_index = pre_index - 1
		check_val = stalls[pre_index]
	
	print_list.append(counter)
	
	for_index = last_index + 1
	check_val = stalls[for_index]
	counter = 0	
	
	while(check_val == 0):
		counter = counter + 1
		for_index = for_index + 1
		check_val = stalls[for_index]
	
	print_list.append(counter)
	
	output_file.write("Case #" + str(l + 1) + ": " + str(max(print_list)) + " " + str(min(print_list)) + "\n")

input_file.close()
output_file.close()
