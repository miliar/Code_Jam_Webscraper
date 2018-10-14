from string import split

#Taking a filename, which refers to a file in the current directory, as input, outputs the text of the file in string format.
def file_to_string(filename):
	filetext = open(filename)
	return filetext.read()

def game_winner(x, r, c):
	if x > 6:
		return "RICHARD"
	if (r*c)%x != 0:
		return "RICHARD"
	if x == 6 or x == 5:
		if r in [1,2,3] or c in [1,2,3]:
			return "RICHARD"
		return "GABRIEL"
	if x == 4:
		if r in [1,2] or c in [1,2]:
			return "RICHARD"
	if x == 3:
		if r == 1 or c == 1:
			return "RICHARD"
	return "GABRIEL"

input = file_to_string("D-small-attempt1.in")
input_lines = split(input, '\n')
num_cases = int(input_lines[0])
arguments = [map(lambda s: int(s), split(l)) for l in input_lines[1:]]
output_file = open("2015_QR_D_output.txt", "w")
for i in range(0, num_cases):
	output_file.write("Case #" + str(i+1) + ": " + game_winner(arguments[i][0], arguments[i][1], arguments[i][2]) + "\n")