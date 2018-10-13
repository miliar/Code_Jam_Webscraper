
	
def read_data(filename):
	file = open(filename)
	x = int(file.readline())
	data = []
	for i in range(x):
		case = file.readline().split()
		for x in range(3):
			case[x] = int(case[x])
		data.append(case)
		
	return data
	
def problem(case):
	test = 0
	today = []
	for possible in range(1,case[0]+1):
		if (possible*(float(case[1])/100))%1 == 0:
			test = 1
			today.append((possible*(float(case[1])/100), possible))
	
	if test == 0:
		return False
	
	if case[2] == 100 and case[1] < 100:
		return False
	if case[2] == 0 and case[1] > 0:
		return False
		
	return True
	
def doit(filename):
	data = read_data(filename)
	file = open('output.out','w')
	case_num = 1
	for case in data:
		if problem(case):
			file.write('Case #%s: Possible\n' % case_num)
		else:
			file.write('Case #%s: Broken\n' % case_num)
		case_num += 1
		
	
	
	
	