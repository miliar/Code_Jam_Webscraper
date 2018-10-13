
def compare_lists(list1, list2):
	potential_numbers = []
	for element1 in list1:
		for element2 in list2:
			if element1 == element2:
				potential_numbers.append(element1)
	return potential_numbers

outputfile = open("C:/Users/Simon/programmering/googlecodejam/outputfile.txt", 'r+') 
lines = open("C:/Users/Simon/programmering/googlecodejam/A-small-attempt1.in", 'r').readlines()

number_samples = int(lines.pop(0))

for number in range (1, number_samples+1):
	line_number1 = int(lines.pop(0))
	line11 = lines.pop(0).split()
	line12 = lines.pop(0).split()
	line13 = lines.pop(0).split()
	line14 = lines.pop(0).split()
	potential_numbers1 = 0
	
	if line_number1 == 1:
		potential_numbers1 = line11
	elif line_number1 == 2:
		potential_numbers1 = line12
	elif line_number1 == 3:
		potential_numbers1 = line13
	elif line_number1 == 4:
		potential_numbers1 = line14
	
	line_number2 = int(lines.pop(0))
	line21 = lines.pop(0).split()
	line22 = lines.pop(0).split()
	line23 = lines.pop(0).split()
	line24 = lines.pop(0).split()
	potential_numbers2 = 0
	
	if line_number2 == 1:
		potential_numbers2 = line21
	elif line_number2 == 2:
		potential_numbers2 = line22
	elif line_number2 == 3:
		potential_numbers2 = line23
	elif line_number2 == 4:
		potential_numbers2 = line24
	
	the_list = compare_lists(potential_numbers1, potential_numbers2)
	if len(the_list) > 1:
		print("Case #" + str(number) + ": Bad magician!")
		outputfile.writelines("Case #" + str(number) + ": Bad magician!")
	elif len(the_list) == 1:
		print("Case #" + str(number) + ": " + the_list[0])
		outputfile.writelines("Case #" + str(number) + ": " + the_list[0])
	elif len(the_list) == 0:
		print("Case #" + str(number) + ": Volunteer cheated!")
		outputfile.writelines("Case #" + str(number) + ": Volunteer cheated!")

		
	