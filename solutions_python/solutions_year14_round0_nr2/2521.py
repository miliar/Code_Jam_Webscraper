file = open('B-large.in')
output = open('output2.txt','w')
lines=int(float(file.readline()))

for x in range(0,lines):
	inpu=[]
	inpu=file.readline().strip().split()
	C=float(inpu[0])
	F=float(inpu[1])
	X=float(inpu[2])
	cookieProd=2.0
	timeNow=0.0
	result=0.0
	while(True):
		nextF=C/cookieProd
		remain1=X/cookieProd
		remain2=X/(cookieProd+F)
		if(nextF+remain2>=remain1):
			result=timeNow+remain1
			break
		timeNow=timeNow+nextF
		cookieProd=cookieProd+F
	# print result
	output.write('Case #'+str(x+1)+': ')
	output.write("%.7f"%result) #str(result))
	output.write('\n')
