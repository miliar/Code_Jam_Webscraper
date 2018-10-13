import re


filename = 'A-small-attempt0.in'
input = open(filename,'r')

cases = int(input.readline())
for testcaseno in range(1,cases+1):
	first_answer = int(input.readline())
	for x in range(1, 5):
		temp = input.readline()
		if x == first_answer:
			first_row = temp
	#print(first_row)

	second_answer = int(input.readline())
	for x in range(1, 5):
		temp = input.readline()
		if x == second_answer:
			second_row = temp
	#print(second_row)

	first_row = first_row[:-1]
	first_row_num = first_row.split(' ')
	map(int, first_row_num)
	#print(first_row_num)

	second_row = second_row[:-1]
	second_row_num = second_row.split(' ')
	map(int, second_row_num)
	#print(second_row_num)

	result = set(first_row_num) & set(second_row_num)

	if len(result) == 1:
		print("Case #" + str(testcaseno) + ": " + str(result.pop()))
	elif len(result) < 1:
		print("Case #" + str(testcaseno) + ": Volunteer cheated!")
	elif len(result) > 1:
		print("Case #" + str(testcaseno) + ": Bad magician!")
