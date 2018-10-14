from string import split

#Given a list "shyness_list" such that shyness_list[i] = # of people with S_i = i, and an integer "max_shyness", the length of shyness_list plus one, num_claqueurs returns the minimum number of additional friends you must invite to the opera to get your friend a standing ovation.
def num_claqueurs(shyness_list, max_shyness):
	curr_shyness = 0
	curr_people = 0
	curr_claqueurs = 0
	while curr_shyness < max_shyness + 1:
		if curr_people < curr_shyness:
			added_claqueurs = curr_shyness-curr_people
			curr_claqueurs += added_claqueurs
			curr_people += added_claqueurs
		curr_people += shyness_list[curr_shyness]
		curr_shyness += 1
	return curr_claqueurs

#Taking a filename, which refers to a file in the current directory, as input, outputs the text of the file in string format.
def file_to_string(filename):
	filetext = open(filename)
	return filetext.read()
	
	
input = file_to_string("A-small-attempt1.in")
input_lines = split(input, '\n')
num_cases = int(input_lines[0])
arguments = [(int(s[0]), [int(s[i]) for i in range(2, int(s[0])+3)]) for s in input_lines[1:num_cases+1]]
output_file = open("2015_QR_A_output.txt", "w")
for i in range(0, num_cases):
	output_file.write("Case #" + str(i+1) + ": " + str(num_claqueurs(arguments[i][1], arguments[i][0])) + '\n')