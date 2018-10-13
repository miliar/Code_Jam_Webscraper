import sys

googlereseToEnglishDictionary = {
	"a" : "y", "b" : "h", "c" : "e", "d" : "s", "e" : "o",
	"f" : "c", "g" : "v", "h" : "x", "i" : "d", "j" : "u",
	"k" : "i", "l" : "g", "m" : "l", "n" : "b", "o" : "k",
	"p" : "r", "q" : "z", "r" : "t", "s" : "n", "t" : "w",
	"u" : "j", "v" : "p", "w" : "f", "x" : "m", "y" : "a",
	"z" : "q", " " : " "
}

def readProblemInputFromFile(fileName):
	input_file  = open(fileName, "r")
	input_lines = []

	for line in input_file:
		input_lines.append(line.replace("\n", ""))

	return input_lines

def solveProblem(input):
	lines_count = int(input[0])
	output	    = []

	for line_number in range(1, lines_count + 1):
		output.append(googlereseToEnglish(input[line_number]))

	return output


def googlereseToEnglish(googlerese_string):
	english_string = ""

	for googlerese_letter in googlerese_string:
		english_string += googlereseToEnglishDictionary[googlerese_letter]
            
	return english_string;


def formatAndPrintOutput(output):
	for line in output:
		print "Case #" + str(output.index(line) + 1) + ": " + line

def main():
	argc  = len(sys.argv)
	input = []

	if argc != 2:
		print 'Usage:', sys.argv[0], '<input file>'

	input  = readProblemInputFromFile(sys.argv[1])
	output = solveProblem(input)

	formatAndPrintOutput(output)

if __name__ == "__main__":
	main()
