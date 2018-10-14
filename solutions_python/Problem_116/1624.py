output=[]
g=[]
def readInput():
	global output,g
	f = open('A-small-attempt0.in', 'r')
	count = f.readline()

	for num in range(1,int(count)+1):
		cur_case =[]
		for line in range(0,4):
			cur_line = f.readline()
			cur_arr = list(cur_line.strip())
			cur_case = cur_case+[cur_arr]
		g=g+[cur_case]
		br = f.readline()
	#o=''.join(g).replace('\n','')

def checkRow(row):
	if ('T' in row and row.count('O')==3) or row.count('O')==4:
		return 'O won'
	elif ('T' in row and row.count('X')==3) or row.count('X')==4:
		return 'X won'
	else:
		return 0
	

def processCase(case):

	if not checkRow([case[0][0],case[1][1],case[2][2],case[3][3]]) ==0:
		return checkRow([case[0][0],case[1][1],case[2][2],case[3][3]])
	if not checkRow([case[0][3],case[1][2],case[2][1],case[3][0]]) ==0:
		return  checkRow([case[0][3],case[1][2],case[2][1],case[3][0]]) 
	#column	
	for j in range(0,4):
		if not checkRow([case[0][j],case[1][j],case[2][j],case[3][j]]) ==0:
			return checkRow([case[0][j],case[1][j],case[2][j],case[3][j]])
	for line in case:
		if '.' in line:
			return 'Game has not completed'
		elif not checkRow(line) ==0:
			return checkRow(line)
	return 'Draw'
def printOutput():
	global g
	fo = open('output_small.txt', 'w')
	for k,case in enumerate(g):

		fo.write('Case #'+str(k+1)+': '+processCase(case)+'\n')
		
readInput()

printOutput()