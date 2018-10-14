import sys

def getInfo():
	file = open(sys.argv[1]);
	a = file.read().split("\n\n");
	
	cases = []
	
	for i in range(len(a)):
		cases.append(a[i].split("\n"));
	
	print cases
	
	
	return cases
	
def solveCase(case):

	#check rows:
	for i in range(4):
		ch = case[i][0]
		if (ch == "."): continue;
		win = True
		for j in range(1, 4):
			if not ((ch == case[i][j]) or (case[i][j] == "T")):
				win = False; break;
		if (win):
			return ch+" won";
		
	#check columns
	for i in range(4):
		ch = case[0][i]
		if (ch == "."): continue;
		win = True
		for j in range(1, 4):
			if not ((ch == case[j][i]) or (case[j][i] == "T")):
				win = False; break;
		if (win):
			return ch+" won";
		
	#check diagonals
	win = True;
	ch = case[0][0]
	for i in range(1, 4):
		if not ((ch == case[i][i]) or (case[i][i] == "T")):
			win = False; break;
	if (ch == "."): win = False;
	if (win): 
		return ch+" won";
	
	win = True;
	ch = case[0][3]
	for i in range(1, 4):
		if not ((ch == case[i][3-i]) or (case[i][3-i] == "T")):
			win = False; break;
	if (ch == "."): win = False;
	if (win): 
		return ch+" won";
		
	#check else
	full = True
	for i in range(4):
		for j in range(4):
			if case[i][j] == '.':
				return "Game has not completed"
	return "Draw"
		
def solveAll(cases, file):
	for i in range(len(cases)):
		file.write("Case #"+str(i+1)+": "+solveCase(cases[i])+"\n")
	
	
if __name__ == "__main__":
	cases = getInfo();
	file = open(sys.argv[1]+".out", 'w');
	solveAll(cases, file);