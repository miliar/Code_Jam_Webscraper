##### Functions Below ##########################################################
def get_matches(list1, list2):
	matches = []
	for l in list1:
		if l in list2:
			matches.append(l)
	return matches


##### Program Logic Below ######################################################

#The filenames of the input and output files
input_path = r"C:\Users\Jake\Documents\~Programming Stuff\Google Code Jam\Competition\Qualification Round\Problem 1\input.txt"
output_path = r"C:\Users\Jake\Documents\~Programming Stuff\Google Code Jam\Competition\Qualification Round\Problem 1\output.txt"

#Read in the text from the input file
input_text = open(input_path, 'r')

#Determine the number of test cases by converting the first line to an int
test_cases = int(input_text.readline())

# Solve each case and output answer to a text file
output_text = open(output_path, 'w')
for c in range(test_cases):	
	answer_one = int(input_text.readline())
	rows = []
	for i in range(4):
		row = input_text.readline()
		row = row.split()
		row = [int(n) for n in row]
		rows.append(row)
	poss_nums = rows[answer_one - 1]

	answer_two = int(input_text.readline())
	rows = []
	for i in range(4):
		row = input_text.readline()
		row = row.split()
		row = [int(n) for n in row]
		rows.append(row)
	poss_nums_two = rows[answer_two - 1]

	matches = get_matches(poss_nums,poss_nums_two)
	num_matches = len(matches)

	text = ""
	if num_matches == 1:
		text = str(matches[0])
	elif num_matches == 0:
		text = "Volunteer cheated!"
	else:
		text = "Bad magician!"
	
	output_text.write("Case #%s: " %(c + 1) + text +"\n")


output_text.close()
