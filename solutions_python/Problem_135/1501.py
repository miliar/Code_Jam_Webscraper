import sys


# Read data file into a list
lines = []
with open(sys.argv[1], "r", encoding="utf-8") as data_file:
	for line in data_file:
		lines.append(line.rstrip('\n'))


# Get total number of test cases
test_cases = int(lines[0])
del lines[0]

# Process each test case
for i in range(test_cases):

	answer_1 = int(lines[0]) - 1
	del lines[0]
	
	possible_1 = []
	for columns in range(4):
		if answer_1 == columns:
			possible_1 = [int(x) for x in lines[0].split(" ")]
		del lines[0]

		
	answer_2 = int(lines[0]) - 1
	del lines[0]
	
	possible_2 = []
	for columns in range(4):
		if answer_2 == columns:
			possible_2 = [int(x) for x in lines[0].split(" ")]
		del lines[0]
		
	
	matches = []
	for j in range(4):
		for k in range(4):
			if possible_1[j] == possible_2[k]:
				matches.append(possible_1[j])
				
	length = len(matches)
	if length == 1:
		result = str(matches[0])
	elif length > 1:
		result = "Bad magician!"
	else:
		result = "Volunteer cheated!"
	print("Case #" + str(i + 1) + ": " + result)
