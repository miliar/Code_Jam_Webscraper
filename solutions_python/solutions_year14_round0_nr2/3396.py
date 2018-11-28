import sys

inFileName = r'C:\GCJ\QUA\B\B-small-attempt0.in' # sys.argv[1]
fileIn = open(inFileName)
fileOut = open(inFileName[:inFileName.rfind('.')] + '.out','w')

nCases=int(fileIn.readline())
for caseNum in range(nCases):
	line = fileIn.readline()

#Start of main logic
	C, F, X = [float(x) for x in line.split()]
	#print(C,F,X)
	idx = 1
	Time = C/2 + X/(2+F)
	PreviousTime = X/2
	while Time <= PreviousTime:
		PreviousTime = Time
		idx += 1
		T = C/2
		for i in range(1, idx): T += C/(2+(i*F))
		Time =  T + X/(2+(idx*F))
		#print('\t', idx, T, PreviousTime, Time)

	out = str(PreviousTime)
#End of main logic

	#print("Case #"+str(caseNum+1)+": "+out+'\n')
	fileOut.writelines("Case #"+str(caseNum+1)+": "+out+'\n')
	fileOut.flush()

fileIn.close()
fileOut.close()
