with open("input.in") as file_in, open("output.out", "w+t") as output_file:
	tests = int(file_in.readline())
	result = []
	count = 1
	for i in file_in:
		number_Tatyana = int(i)
		number = 1
		last_number = 1
		while(number<=number_Tatyana):
			is_True = True
			if(not('0' in str(number))):
				numbers_list = list(str(number))
				for c in range(len(numbers_list)-1):
					if(int(numbers_list[c]) > int(numbers_list[c+1])):
						is_True = False
						break
			else:
				is_True = False
			
			if(is_True):
				last_number = number
			
			number += 1
			
						
		output_file.write("Case #{}: {}\n".format(count, last_number))
				
				
		
		count += 1 
		