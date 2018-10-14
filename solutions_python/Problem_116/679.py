def checkCase(file):
	line1 = file.readline()
	line2 = file.readline()
	line3 = file.readline()
	line4 = file.readline()
	file.readline() #discard empty line
	
	incomplete = False;
	#check rows
	for line in [line1,line2,line3,line4]:
		(bool,val) = checkFour(line)
		if bool:
			return val + " won"
		elif val == 'Incomplete':
			incomplete = True;
	
	#check cols
	for col in [0,1,2,3]:
		(bool,val) = checkFour([line1[col],line2[col],line3[col],line4[col]])
		if bool:
			return val + " won"
		elif val == 'Incomplete':
			incomplete = True;
	
	#check diags
	(bool,val) = checkFour([line1[0],line2[1],line3[2],line4[3]])
	if bool:
		return val + " won"
	elif val == 'Incomplete':
		incomplete = True;

	(bool,val) = checkFour([line1[3],line2[2],line3[1],line4[0]])
	if bool:
		return val + " won"
	elif val == 'Incomplete':
		incomplete = True;
	
	if incomplete:
		return "Game has not completed"
	else:
		return "Draw"


def checkFour(line):
	#assert line = [a,b,c,d,\n]
	xCount = line.count('X')
	if xCount == 4:
		return (True,'X')
	elif xCount == 3:
		if 'T' in line:
			return (True,'X')
	else:
		yCount = line.count('O')
		if yCount == 4:
			return (True,'O')
		elif yCount == 3:
			if 'T' in line:
				return (True,'O')

	if '.' in line:
		return (False,'Incomplete');
	
	return (False, None)

file = open('A-large.in');
numCases =  int(file.readline())
for case in range(numCases):
	print "Case #"+str(case+1)+": "+checkCase(file)
