#Google Code Jam Alien problem
#Bhaktavatsalam Nallanthighal, New York
#Sep 3 2009

dummyitem = ""

def contained(item): return item.startswith(dummyitem)

params = raw_input().split()

length = int(params[0])
numwords = int(params[1])
testcases = int(params[2])

words = []
dictwords = {}
posbposletters = []

def noOfMatches(theString, posindex, index):
	global posbposletters
	global dummyitem

	count = 0	
	for b in range(len(posbposletters[posindex])):
		dummystring = theString + posbposletters[posindex][b]
		dummyitem = theString + posbposletters[posindex][b]
	
		matches = filter(contained, dictwords.keys())
	
		if len(matches)>0:
			if posindex == (len(posbposletters)-1):
				count += len(matches)
			else:
				count += noOfMatches(dummystring, posindex+1, 0)
			
	return count


for i in range(numwords):
	temp = raw_input()
	for j in range(len(temp)):
		if j >= len(words):
			aHash = {}
			words.append(aHash)
		words[j][temp[j]] = ""
	dictwords[temp] = ""
	
for i in range(testcases):
	temp=""
	temp = raw_input()
	
	k=0
	actualStrLen = 0
	confirmCasesZero = False
	possiblewords = []
	possiblewordsAsList = []
	possibleposletters = []
	
	#possible letter positions
	while k < len(temp):
		possibleletters = []
		if temp[k] == '(' :
			k+=1
			while temp[k]!=')':
				if(words[actualStrLen].has_key(temp[k])):
					possibleletters.append(temp[k])
				k+=1
			
			if possibleletters == []:
				confirmCasesZero = True
			
			possibleposletters.append(possibleletters)
		else:
			if(words[actualStrLen].has_key(temp[k])):
				possibleposletters.append(temp[k])
			else:
				confirmCasesZero = True
		k+=1
		actualStrLen+=1
		
		if confirmCasesZero:
			break
		
	if confirmCasesZero:
		print "Case #" + str(i+1) + ": 0"
		continue
		
	posbposletters = possibleposletters
	
	print "Case #" + str(i+1) + ":", noOfMatches("", 0, 0)
