infile = open("A-small-attempt2.in", "r")
f = open('out2.txt', 'w')
lines = infile.read().strip()
input = ""
for line in lines:
	input = input + line
input = input.replace("\n", " ")
count = 1
nb_cases = input[0]
while (input[0 + count] != " "):
	nb_cases = nb_cases + input[count]
	count = count + 1
i = 0
while (i < int(nb_cases)):
	first_card = input[len(nb_cases) + 1 + i*82]
	second_card = input[len(nb_cases) + 42 + i*82]
	row1 = []
	row2 = []
	spaces_required1 = 4*(int(first_card)-1)+1
	spaces = 0
	starting_point1 = len(nb_cases) + 1 + i*82
	while (spaces != spaces_required1):
		if input[starting_point1] == " ":
			starting_point1 = starting_point1 + 1
			spaces = spaces + 1
		else :
			starting_point1 = starting_point1 + 1
	spaces = 0
	while (spaces < 4):
		if input[starting_point1] != " ":
			if input[starting_point1+1] == " ":
				row1.extend(input[starting_point1])
				starting_point1 = starting_point1 + 1
			else:
				string_to_add = input[starting_point1]+input[starting_point1+1]
				row1.append(string_to_add)
				starting_point1 = starting_point1 + 2
		else:
			starting_point1 = starting_point1 + 1
			spaces = spaces + 1
	spaces_required2 = 4*(int(second_card)-1)+1
	starting_point2 = len(nb_cases) + 42 + i*82
	spaces = 0
	while (spaces != spaces_required2):
		if input[starting_point2] == " ":
			starting_point2 = starting_point2 + 1
			spaces = spaces + 1
		else :
			starting_point2 = starting_point2 + 1
	spaces = 0
	while (spaces < 4):
		if starting_point2 < len(input):
			if input[starting_point2] != " ":
				if input[starting_point2+1] == " ":
					row2.extend(input[starting_point2])
					starting_point2 = starting_point2 + 1
				else:
					string_to_add = input[starting_point2]+input[starting_point2+1]
					row2.append(string_to_add)
					starting_point2 = starting_point2 + 2
			else:
				starting_point2 = starting_point2 + 1
				spaces = spaces + 1
		else:
			break
	common_elements = []
	for element1 in row1:
		for element2 in row2:
			if element1 == element2:
				common_elements.append(element1)
	if len(common_elements) == 1:
		print >> f, "Case #%s: %s" % (i+1, common_elements[0])
	elif len(common_elements) == 0:
		print >> f, "Case #%s: Volunteer cheated!" % (i+1)
	else:
		print >> f, "Case #%s: Bad magician!" % (i+1)
	i = i + 1



"""
3 2 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 3 1 2 5 4 3 11 6 15 9 10 7 12 13 14 8 16 2 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 2 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 2 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 3 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
"""