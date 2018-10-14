def read_file():
	f = open("A-large.in", 'r')
	num_case = int(f.readline())
	
	for n in range(num_case):
		row_input = f.readline()
		row_split = row_input.split()
		max_s = int(row_split[0])
		audience = row_split[1]
		max_aud = 0
		num_friends = 0
		
		for i in range(max_s+1):		
			max_aud += int(audience[i])

			if((i+1-max_aud)>0):
				num_friends+=1
				max_aud += 1
		
		print_result(n+1, num_friends)
	
def print_result(case, num_friends):
	print('Case #{}: {}'.format(case,num_friends))
		
read_file()
