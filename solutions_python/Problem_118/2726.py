import math

def process_file(f):
	''' This function processes the given file. '''

	fIn = open(f, "r");

	fLine = fIn.readline()
	numCases = int(fLine.strip())
	case_dict = {}
	case_counter = 1;

	fLine = fIn.readline()
	while case_counter <= numCases and fLine:
		case = fLine.strip().split()
		for i in range(len(case)):
			case[i] = int(case[i])

		case_dict[case_counter] = case
		case_counter += 1
		fLine = fIn.readline()

	fIn.close()
	return case_dict

def process_cases(cases):
    ''' This function goes through all the game cases. 
        Once the results are received it is written into a text file.'''

    fOut = open('output.txt', 'w')

    for key in range(1, len(cases.keys()) + 1):
    	res = process_case(cases[key])
    	fOut.write("Case #" + str(key) + ": " + str(res) + "\n")
    	print "Case #" + str(key) + " " + str(res)

    fOut.close()

def process_case(case):
	''' Check number of fair and square within the given range. '''

	num_fs = 0

	for val in range(case[0], case[1] + 1):
		sqrted = str(math.sqrt(val))
		if sqrted.endswith(".0"):
			sqrted = sqrted[:sqrted.find(".0")]
			sqL = []
			inValL = []
			for num in str(sqrted):
				sqL.append(int(num))
			for num in str(val):
				inValL.append(int(num))
		
			if check_palindrome(sqL) and check_palindrome(inValL):
				num_fs += 1
	return num_fs

def check_palindrome(valL):
	endInd = -1

	for i in range(len(valL)):
		if valL[i] != valL[endInd]:
			return False
		endInd -= 1

	return True

if __name__ == "__main__":
    case = process_file("C-small-attempt1.in")
    process_cases(case)