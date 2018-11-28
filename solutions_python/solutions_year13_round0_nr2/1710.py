def process_file(f):
	''' This function processes the given file. '''

	fIn = open(f, "r");

	fLine = fIn.readline()
	numCases = int(fLine.strip())
	case_dict = {}
	case_counter = 1;

	fLine = fIn.readline()
	while fLine and case_counter <= numCases:
		size = fLine.strip().split()
		n = int(size[0])
		m = int(size[1])
		n_counter = 1
		mainL = []

		fLine = fIn.readline()
		while fLine and n_counter <= n:
			row = fLine.strip().split()
			mainL.append(row)
			n_counter += 1
			fLine = fIn.readline()

		t = (n, m, mainL)
		case_dict[case_counter] = t
		case_counter += 1

	fIn.close()

	return case_dict

def process_cases(cases):
    ''' This function goes through all the game cases. 
        Once the results are received it is written into a text file.
    '''

    fOut = open('output.txt', 'w')

    for key in range(1, len(cases.keys()) + 1):
        res = process_case(cases[key])
        if res:
        	fOut.write("Case #" + str(key) + ": " + "YES\n")
        	print "Case #" + str(key) + ": " + "YES"
        else:
        	fOut.write("Case #" + str(key) + ": " + "NO\n")
        	print "Case #" + str(key) + ": " + "NO"

    fOut.close()
        
def process_case(case):
	''' Mow lawn to target lawn. '''

	new_lawn = create_lawn(case[0], case[1], get_max(case[2]))
	target_lawn = case[2]

	# Mow lawn horizontally.
	for x in range(case[0]):
		h = get_max_row_check(target_lawn, x) 
		if h != -1:
			for i in range(case[1]):
				new_lawn[x][i] = h

	# Check target_lawn == new_lawn.
	if check_new_lawn(new_lawn, target_lawn, case[0], case[1]):
		return True
	
	# Mow lawn vertically.
	for y in range(case[1]):
		h = get_max_col_check(target_lawn, y, case[0])
		if h != -1:
			for x in range(case[0]):
				new_lawn[x][y] = h
	
	# Check target_lawn == new_lawn.
	if check_new_lawn(new_lawn, target_lawn, case[0], case[1]):
		return True
	return False

def create_lawn(n, m, maxH):
	''' Creates new lawn with grass height is maxH. '''

	mainL = []
	for x in range(n):
		subL = []
		for y in range(m):
			subL.append(maxH)
		mainL.append(subL)

	return mainL

def get_max(case):
	''' Returns the max height in the target lawn. '''

	l = []
	for ele in case:
		l += ele

	return max(l)

def get_max_row_check(case, row):
	''' This function checks and returns the max height at row. '''

	m = max(case[row])

	for val in case[row]:
		if val != m:
			return -1
	return m

def get_max_col_check(case, col, h):
	''' This function checks and return the max height at column col. '''

	m = -1

	for x in range(h):
		if case[x][col] > m:
			m = case[x][col]

	for x in range(h):
		if case[x][col] != m:
			return -1
	return m

def check_new_lawn(new_lawn, target_lawn, n, m):
	''' This function checks if the target lawn and new lawn is the same. '''

	for x in range(n):
		for y in range(m):
			if new_lawn[x][y] != target_lawn[x][y]:
				return False
	return True

if __name__ == "__main__":
    case = process_file("B-small-attempt0.in")
    process_cases(case)
