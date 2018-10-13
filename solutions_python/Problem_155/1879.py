def readInputFile():
	l = [line.rstrip('\n') for line in open('qualiA.in')]
	return l

def putOutputFile(lines):
	f = open('qualiA.out', 'w')
	for row in lines:
 		f.write('%s\n' % row)

def howManyFriendsToAdd(audience):
	standing = 0
	need = 0

	for i in range(int(audience[0])+1):
		n = int(audience[i+2]) #skip 'x ' at the beginning
		if i > standing: # shy level is higher than #standing people
			need += 1
			standing += 1
		standing += n

	return need



lines = readInputFile()

# print(lines[0]+' Cases')

outputCaseResults = [howManyFriendsToAdd(audience) for audience in lines[1::]]
generatedOutput = list()

i = 1
for o in outputCaseResults:
	# print('Case #' + str(i) + ': ' + str(o))
	generatedOutput.append('Case #' + str(i) + ': ' + str(o))
	i+=1

putOutputFile(generatedOutput)