#########################
#		MAGICKA			#
#########################

def magicka_problem(filename):
	
	data = read_in_data(filename)
	
	file = open('output.out', 'w')
	
	for case in range(len(data)):
		
		element_list = find_element_list(data[case])
		
		file.write('Case #')
		file.write(str(case+1))
		file.write(': ')
		file.write(str(element_list).replace("'",""))
		file.write('\n')
		
		#value = 'Case #' + str(case+1) + ': ' + str(element_list)
		#value.replace("\'","")
		#file.write(value+'\n')
		
	file.close()



def read_in_data(filename):
	'''
	the file will be read and constructed
	into a useful data construct, which in this case
	will be a list of cases, where each case will contain
	3 elements. The first will be a dictionary of combinations,
	where the keys are the elements that can combine and the value
	is the output of that combination. The 2nd element will be a list
	of opposing elements. Finally the 3rd will be the element list itself.
	'''
	file = open(filename)
	x = int(file.readline())	### x is the number of test cases
	
	data = []
	
	for i in range(x):
		
		case = [{},[]]
		templine = file.readline()
		templine = templine.split()
		
		index = 0
		
		### configure the combination dictionary
		combinations = []
		
		for i in range(int(templine[index])):
			combinations.append(templine[i+1])
			
		for combination in combinations:
			case[0][combination[:2]] = combination[2]
			case[0][combination[1]+combination[0]] = combination[2]
			
			
		### configure the opposition list	
		index += int(templine[index]) + 1 		### move to the oppositions
		
		for i in range(int(templine[index])):
			case[1].append(templine[i+index+1])
		
		
		### now append the actual element list
		index += int(templine[index]) + 2
		
		case.append(templine[index])
			
		data.append(case)
		
	file.close()
		
	return data
	
	
def find_element_list(test_case):
	
	element_list = []	### element_list will hold our answer
	
	index = 0		### this will help with placeholding
	
	### rename variables for clarity
	combinations = test_case[0]
	oppose = test_case[1]
	elements = test_case[2]
	
	while index < len(elements):
	
		element_list.append(elements[index])
		
		
		if len(element_list) > 1:
	
			if element_list[len(element_list)-1]+element_list[len(element_list)-2] in combinations:
				element_list.pop()
				element_list.pop()
				element_list.append(combinations[elements[index]+elements[index-1]])
				
			for opposition in oppose:
				if opposition[0] in element_list and opposition[1] in element_list:
					element_list = []
		
		index += 1
		
	return element_list
		
		
		