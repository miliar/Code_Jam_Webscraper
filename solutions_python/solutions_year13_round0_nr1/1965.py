def matchdia(case, char):
	dia = True
	for i in range(0,4):
		if (case[i][i] != char and case[i][i] != "T"):
			dia= False
			break
	if dia: return dia

	dia = True
	for i in range(0,4):
		if (case[i][3-i] != char and case[i][3-i] != "T"):
			dia = False
			break
	return dia	
			


def matchver(case,char):
	for i in range(0,4):
		hor = True
		for j in range(0, 4):
			if (case[j][i] != char and case[j][i] != "T"):
				hor = False
				break
		if(hor): break
	return hor

def matchhor(case,char):
	for i in range(0,4):
		hor = True
		for j in range(0, 4):
			if (case[i][j] != char and  case[i][j] != "T"):
				hor = False
				break
		if(hor): break
	return hor



def subprocess(case):
	if(matchhor(case,"X")): return 1
	elif(matchhor(case,"O")): return 2
	elif(matchver(case,"X")): return 1
	elif(matchver(case, "O")): return 2
	elif(matchdia(case, "X")): return 1
	elif(matchdia(case,"O")): return 2
	else: return 3

def process(case,testcasecount):
	#print case
	flag =0
	result = 0
	for i in range(len(case)):
		for j in range(0,4):
			#print case[i][j]
			if case[i][j] == ".": flag = 1

	result = subprocess(case) 
	if result == 1: # X won
		strres ="X won"
	elif result == 2: # O won
		strres = "O won"
	elif flag ==0:
		strres ="Draw"
	else:
		strres = "Game has not completed"

	s = "Case #"
	s+=str(testcasecount+1)
	s+=": "
	s+=strres
	print s

with open("test.txt","r") as fs:
	count = int(fs.readline())
	for testcasecount in range(0,count):
		case = []
		t = fs.readline()
		#print t
		for i in range(0,4):
			#print t
			x = [t[n] for n in range(len(t)-1)]
			case.append(x)
			t = fs.readline()
		#print case
		process(case,testcasecount)
		testcasecount-=1

