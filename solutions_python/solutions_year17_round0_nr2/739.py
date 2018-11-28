def is_tidy(number):
	num_str = str(number)
	for i in range(len(num_str)-1):
		if int(num_str[i]) > int(num_str[i+1]):
			return False		
	return True

cases = int(input())

for i in range(cases):
	last_num = int(input())
	sub_factor = 1
	next_sub_factor = 10
	while True:
		if is_tidy(last_num):
			print('Case #{}: {}'.format(i+1,last_num))
			break
		
		if (last_num+1) % next_sub_factor == 0:
			sub_factor = next_sub_factor
			next_sub_factor *= 10
			
		
		last_num -= sub_factor
			

	
	
	