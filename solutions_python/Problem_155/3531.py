inputFile = open('input','r')
outputFile = open('output','w')

def outputGen(line):
	s_max = int(line[0])
	if(s_max == 0 ):
		return 0
	
	standing = int(line[2])
	if standing >= s_max:
			return 0
	required = 0

	for k in xrange(1,s_max+1):
		if standing >= k:
			standing += int(line[k+2])
		else:
			required+= k-standing
			standing += k-standing+int(line[k+2])
	return required

totalcases = int(inputFile.readline())
for case in xrange(totalcases-1):
	line = inputFile.readline()
	outputFile.write("Case #"+str(case+1)+": "+ str(outputGen(line))+'\n')
line = inputFile.readline()
outputFile.write("Case #"+str(totalcases)+": "+ str(outputGen(line)))


inputFile.close()
outputFile.close()

