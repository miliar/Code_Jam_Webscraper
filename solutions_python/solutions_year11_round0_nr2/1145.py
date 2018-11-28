
infile = "B-small-attempt2.in"
#infile = "input.txt"
input = open(infile, "r")
outfile = "magika.txt"
output = open(outfile, "w")

test_cases = input.readline()
test_cases = int(test_cases)


for i in range(1, (test_cases+1)):
	element_list = []
	line = input.readline().rstrip("\n").split(' ')	
	number_combinations = line[0]
	number_combinations = int(number_combinations)
	line.pop(0)
	
	combinations = {}
	if number_combinations != 0:
		for k in range (0, number_combinations):
			combo_string = line[0]
			line.pop(0)
			elements_forward = combo_string[0]+combo_string[1]
			elements_backward = combo_string[1]+combo_string[0]
			result = combo_string[2]
			combinations[elements_forward] = result
			combinations[elements_backward] = result	


	number_opposed = line[0]
	number_opposed = int(number_opposed)
	line.pop(0)
	opposed_list = []
	opposed_dictionary = {}
	if number_opposed != 0:
		for k in range (0, number_opposed):
			combo_string = line[0]
			line.pop(0)
			letter1 = combo_string[0]
			opposed_list.append(letter1)
			letter2 = combo_string[1]
			opposed_list.append(letter2)
			opposed_dictionary[letter1] = letter2
			opposed_dictionary[letter2] = letter1
			combo1 = letter1 + letter2
			combo2 = letter2 + letter1
			opposed_list.append(combo1)
			opposed_list.append(combo2)


	number_instring = line[0]
	number_instring = int(number_instring)
	line.pop(0)
	my_data = line[0]
	line.pop(0)

	previous = ""
	working_opposed = []
	my_output = []
	for k in range(0, number_instring):
		current = my_data[k]
		two_chars1 = previous + current
		two_chars2 = current + previous
		if combinations.has_key(two_chars1):
			my_output.pop()
			current = combinations[two_chars1]
			previous = current
			my_output.append(current)		
		elif combinations.has_key(two_chars2):
			my_output.pop()
			current = combinations[two_chars2]		
			previous = current
			my_output.append(current)
		elif current in opposed_list:
			opp = opposed_dictionary[current]		
			if opp in my_output:
				my_output = []
				previous = ""
#				remove_here = my_output.index(opp)
#				temp = []
#				for j in range (0, remove_here):
#					if j < remove_here:
#						save_it = my_output[j]
#						temp.append(save_it)
#				my_output = temp
#				if len(my_output) > 0:
#					length = len(my_output) - 1
#					previous = my_output[length]
#				else:
#					previous = ""
			else:
				previous = current
				my_output.append(current)
		else:
			previous = current								
			my_output.append(current)

	number = str(i)
	output.write("Case #"+number+": ",)
	output.write('[')
	for k in range(0, len(my_output)):
		item = my_output[k]
		output.write(item)
		if k < (len(my_output)-1):
			output.write(", ")
	output.write(']')
	output.write('\n')


input.close()
output.close()
