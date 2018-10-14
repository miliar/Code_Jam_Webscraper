###########################
#		Candy Splitting	  #
###########################

def candy_problem(filename):
	
	data = read_in_data(filename)
	
	file = open('output.out', 'w')
	
	case_num = 1
	
	for case in data:
		
		answer = split_candy(case)
		
		file.write('Case #')
		file.write(str(case_num))
		file.write(': ')
		file.write(str(answer))
		file.write('\n')
		
		case_num+= 1
		
	
def read_in_data(filename):
	'''
	returns a list of lists, where each nested list is one test case,
	containing all of the candy values
	'''
	file = open(filename)
	x = int(file.readline())	### x is the number of test cases
	data = []
	for i in range(x):
		
		case = []
		templine = file.readline()	### reads the number of candies
		templine = file.readline()	### gets the candy values
		templine = templine.split()	### split the values
			
		for value in templine:
			case.append(int(value))
			
		data.append(case)
		
	file.close()
		
	return data
	
	
def split_candy(case):
	
	### check if spliting is possible
	if not is_split_possible(case):
		return 'NO'
		
	patrick = []
	sean = []
	
	### if everything adds to 0, then you just have to give
	### patrick the smallest one, so his pile is not empty and
	### give sean the rest, which will all add up to the same thing
	
	case.remove(min(case))
	answer = sum(case)
	return answer
		
		
def is_split_possible(case):
	
	sum = 0
	
	for value in case:
		
		sum = patrick_add(sum, value)
		
	if sum == 0:
		return True
	else:
		return False

	

def patrick_add(number_1,number_2):
	
	num_1_b = bin(number_1)[2:]
	num_2_b = bin(number_2)[2:]
	
	answer = '0b'	### build the answer onto this base
	
	### Sign extend the smaller value if not of equal length
	if len(num_2_b) != len(num_1_b):
		
		if len(num_2_b) < len(num_1_b):
			
			for i in range(len(num_1_b)-len(num_2_b)):
				
				num_2_b = '0' + num_2_b
		
		
		if len(num_1_b) < len(num_2_b):
			
			for i in range(len(num_2_b)-len(num_1_b)):
				
				num_1_b = '0' + num_1_b
				
	index = 0
	
	while index < len(num_1_b):		### They are now same length so doesn't matter which one is picked
	
		if set((num_1_b[index],num_2_b[index])) == set(('0')):
			answer += '0'
			
		if set((num_1_b[index],num_2_b[index])) == set(('1')):
			answer += '0'
			
		if set((num_1_b[index],num_2_b[index])) == set(('0','1')):
			answer += '1'
			
		index += 1
		
	sum = int(answer, 2)
	
	return sum
	
	
	
		
		
		
		
	
	