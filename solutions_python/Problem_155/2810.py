import sys

fout = open("outputfile" , "w+b")

f=open(sys.argv[1])

TCases = int(f.readline()[0:-1])

for i in range(0, TCases):

	lineCaseSplit = f.readline().split(" ")
	
	lenCase = int(lineCaseSplit[0])+1
	
	curCase = lineCaseSplit[1][0:-1]
	
	nClapping = 0
	nNeeded = 0
	
	for j in range(0, lenCase):
	
		if j > nClapping:		
			nNeeded += (j - nClapping)
			nClapping += (j - nClapping)
		
		nClapping += int(curCase[j])
	
	fout.write ("Case #%d: %d\r\n" % (i+1, nNeeded))
	
fout.close()
		
		
	

