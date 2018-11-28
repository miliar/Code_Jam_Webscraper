import sys

def magic(i, first, array1, second, array2):
	print("Case #" + str(int(i/10)) + ": ", end = "")
	first_choice = array1[4*(first - 1):4*first]
	second_choice = array2[4*(second - 1):4*second]
	intersection = []
	for each in first_choice:
		if each in second_choice:
			intersection.append(each)
	if (len(intersection) == 1):
		print(intersection[0])
	elif (len(intersection) > 1):
		print("Bad magician!")
	elif (len(intersection) < 1):
		print("Volunteer cheated!")

i = 0
first_array = []
second_array = []
first_row = 1
second_row = 1
for every_line in sys.stdin:
	if (i == 0):
		i += 1
		continue
	if (i % 10 == 1):
		first_row = int(every_line)
	elif (i % 10 == 2 or i % 10 == 3 or i % 10 == 4 or i % 10 == 5):
		for each in every_line.strip("\n").split(" "):
			first_array.append(int(each))
	elif (i % 10 == 6):
		second_row = int(every_line)
	elif (i % 10 == 7 or i % 10 == 8  or i % 10 == 9 or i % 10 == 0):
		for each in every_line.strip("\n").split(" "):
			second_array.append(int(each))
	if (i % 10 == 0):
		magic(i, first_row, first_array, second_row, second_array)
		first_array = []
		second_array = []
	i += 1