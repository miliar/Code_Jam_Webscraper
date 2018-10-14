
inFile = open('./B-large.in', 'r')
outFile = open('./output.out', 'w')
caseNum = int(inFile.readline())
for num in range(1, caseNum + 1) :

	vecStr = inFile.readline().split(' ')
	c = float(vecStr[0])
	f = float(vecStr[1])
	x = float(vecStr[2])
	g = 2
	time = c/g
	
	if x <= c :
		print('Case #%d: %.7f' %(num,x/g), file = outFile)
		continue
		
	while (x-c)/g > x/(g+f) :
		g += f
		time += c/g
	print('Case #%d: %.7f' %(num,time+(x-c)/g), file = outFile)
