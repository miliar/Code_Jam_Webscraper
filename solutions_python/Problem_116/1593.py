file = open("input.txt", "r")
out = open("output.txt", "w")
n = 0

def check(a):
	L1 = []
	L2 = []

	#X check
	for i in range(4):
		temp = []
		for j in range(4):
			if a[i][j] != 'T':
				temp.append(a[i][j])
			else:
				temp.append('X')
		L1.append(temp)



	
	for i in L1:
		if 'O' not in i:
			if '.' not in i:
				return 'X won'

	for i in range(4):
		if L1[0][i] == 'X' and L1[1][i] == 'X' and L1[2][i] == 'X' and L1[3][i] == 'X':
			return 'X won'
	if L1[0][0]=='X' and L1[1][1]=='X' and L1[2][2]=='X' and L1[3][3]=='X':
		return 'X won'
	if L1[0][3]=='X' and L1[1][2]=='X' and L1[2][1]=='X' and L1[3][0]=='X':
		return 'X won'

	#O check
	for i in range(4):
		temp = []
		for j in range(4):
			if a[i][j] != 'T':
				temp.append(a[i][j])
			else:
				temp.append('O')
		L2.append(temp)



	for i in L1:
		if 'X' not in i:
			if '.' not in i:
				return 'O won'

	for i in range(4):
		if L2[0][i] == 'O' and L2[1][i] == 'O' and L2[2][i] == 'O' and L2[3][i] == 'O':
			return 'O won'
	if L2[0][0]=='O' and L2[1][1]=='O' and L2[2][2]=='O' and L2[3][3]=='O':
		return 'O won'
	if L2[0][3]=='O' and L2[1][2]=='O' and L2[2][1]=='O' and L2[3][0]=='O':
		return 'O won'
	draw = True
	#else
	for i in range(4):
		for j in range(4):
			if L1[i][j] == '.':
				draw = False

	if draw == True:
		return 'Draw'
	else:
		return 'Game has not completed'

def getlist():
	list1 = []
	for i in range(n):
		temp = []
		a = file.readline()
		temp.append(a)
		a = file.readline()
		temp.append(a)
		a = file.readline()
		temp.append(a)
		a = file.readline()
		temp.append(a)
		file.readline()
		list1.append(temp)
	return list1



def func():
	global n
	temp1 = file.readline()
	n = int(temp1)
	L = getlist()
	print n,L
	for i in range(n):
		a = check(L[i])
		print "Case #" + str(i+1) + ":" + a
		out.write("Case #" + str(i+1) + ":" + a + "\n")


func()