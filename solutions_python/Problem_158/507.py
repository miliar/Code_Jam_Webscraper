def inputFromFile():
	filename = "A-small-practice.in"
	filepath = "/home/sayan/Downloads/"
	url = filepath + filename
	inp = []
	f = open(url, 'r')
	test_cases = int(f.readline()) 
	for dummy_num in range(test_cases):
		first_ans = int(f.readline()) - 1
		init_grid = []
		shuf_grid = []
		for dummy_row in range(4):
			init_grid.append(list(map(int, f.readline().split())))
		second_ans = int(f.readline()) - 1
		for dummy_row in range(4):
			shuf_grid.append(list(map(int, f.readline().split())))
		set1 = set(init_grid[first_ans])
		set2 = set(shuf_grid[second_ans])
		inp.append(list(set1.intersection(set2)))	
	return inp

def inputFromTerminal():
	inp = []
	test_cases = int(raw_input()) 
	for dummy_num in range(test_cases):
		x, r, c = map(int, raw_input().split())
		if x > r * c or (r * c) % x != 0:
			inp.append(0)
		elif x == 1 or x == 2:
			inp.append(1)
		elif r < x - 1 or c < x - 1:
			inp.append(0)
		elif x >= 7:
			inp.append(0)
		else:
			inp.append(1)
	return inp
	
def output(intsc):
	case = "Case #"
	gab = "GABRIEL"
	rich = "RICHARD"
	oup = []
	for dummy_num in range(len(intsc)):
		if intsc[dummy_num]:
			oup.append(case + str(dummy_num + 1) + ": " + gab)
		else:
			oup.append(case + str(dummy_num + 1) + ": " + rich)
	return oup

def printToTerminal(oup):
	for string in oup:
		print string
		
def printToFile(oup):
	f = open('/home/sayan/Desktop/output.txt', 'w')
	for string in oup:
		f.write(string + '\n')
		
#printToFile(output(inputFromFile()))
printToTerminal(output(inputFromTerminal()))
