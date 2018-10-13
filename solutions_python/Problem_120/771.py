fileName= raw_input("Name of the input file or full path:  ")
inFile=open(fileName,'r')
tCases=inFile.readlines()
results=[]

for case in tCases[1:]:
	ringOrder=0
	totalRings=0
	caseData=case.rstrip().split(' ')
	rad=int(caseData[0])
	vol=int(caseData[1])
	ringSize=rad*rad
	
	i=0
	value=(rad+i)*(rad+i)-((rad+i-1)*(rad+i-1))
	while value<=vol:
		if ringOrder%2==1:
			totalRings+=1
			vol-=value
		i+=1
		value=(rad+i)*(rad+i)-((rad+i-1)*(rad+i-1))
		ringOrder+=1
	results.append(totalRings)

count=1
outputFile=open(fileName.split('.')[0]+'.out','a')
for e in results:
	if count>1:
		outputFile.write('\n')
	outputFile.write('Case #'+str(count)+': '+str(e))
	count+=1
outputFile.close()
raw_input('close?')