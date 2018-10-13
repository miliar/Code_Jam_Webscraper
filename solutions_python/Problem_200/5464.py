def tidy_numbers(input_data):
	test_case_number = input_data[0]
	i = 1 
	for test_number in range(int(test_case_number)):
		last_number_counted = input_data[i]
		for number in range(int(last_number_counted),0,-1):
			str_num = str(number)
			previous_character = 0
			tidy = True
			for current_character in str_num:
				if int(previous_character) > int(current_character):
					tidy = False
				else:
					previous_character = int(current_character)
			if tidy == True:
				output = str(number)
				break
		answer = ("Case #"+str(i)+": "+output)
		print(answer)
		i+= 1



def open_file():
	with open("./tidynumbers.txt") as f:
		input = f.readlines()
		input = [x.strip() for x in input]
		tidy_numbers(input)




open_file()