import math

fileName=raw_input("Name of the input file or full path:")
fileHandle=open(fileName,'r')

allLines=fileHandle.readlines()
fileHandle.close()

intervals=[]
for line in allLines[1:]:
	line.rstrip()
	intermediate=line.split()
	intervals.append([int(intermediate[0]), int(intermediate[1])])

count=0
outputFile=open(fileName.split('.')[0]+'.out','a')
for interval in intervals:
	count+=1
	if count>1:
		outputFile.write('\n')
	fairSquare=0
	for i in range(interval[0],interval[1]+1):
		root=math.sqrt(i)
		if math.ceil(root)==root:
			root=int(root)
			hasRoot=True
		else:
			hasRoot=False
		if hasRoot:
			if str(i)==str(i)[::-1] and str(root)==str(root)[::-1]:
				fairSquare+=1
	outputFile.write('Case #'+str(count)+': '+str(fairSquare))

outputFile.close()