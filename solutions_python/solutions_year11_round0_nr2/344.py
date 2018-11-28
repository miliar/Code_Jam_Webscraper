from collections import deque

file = open("B-large.in")
strWholeFile = file.read()
aStrLines = strWholeFile.split("\n")

nCases = int(aStrLines[0])

for nCase in range(1, nCases + 1):
	aChTokens = aStrLines[nCase].split()
	dequeTokens = deque(aChTokens)
	
	dictMerge = dict()
	nMerge = int(dequeTokens.popleft())
	
	for _ in range(0, nMerge):
		strMerge = dequeTokens.popleft()
		
		dictMerge[strMerge[0] + strMerge[1]] = strMerge[2]
		dictMerge[strMerge[1] + strMerge[0]] = strMerge[2]
	
	dictOpp = dict()
	nOpp = int(dequeTokens.popleft())
	
	for _ in range(0, nOpp):
		strOpp = dequeTokens.popleft()
		if not strOpp[0] in dictOpp:
			dictOpp[strOpp[0]] = []
		dictOpp[strOpp[0]].append(strOpp[1])
		
		if not strOpp[1] in dictOpp:
			dictOpp[strOpp[1]] = []
		dictOpp[strOpp[1]].append(strOpp[0])
	
	dequeTokens.popleft()
	dequeCommand = deque(dequeTokens.popleft())
	aryBuffer = []
	
	while dequeCommand:
		chCur = dequeCommand.popleft()
		chLastChecked = None
		while aryBuffer and chCur != chLastChecked:
			chLastChecked = chCur
			chLast = aryBuffer[-1]
			strLookup = chLast + chCur
			if strLookup in dictMerge:
				aryBuffer.pop()
				chCur = dictMerge[strLookup]
			
		if chCur in dictOpp:
			for chOpp in dictOpp[chCur]:
				if chOpp in aryBuffer:
					aryBuffer = []
					chCur = None
					break
					
		if chCur:
			aryBuffer.append(chCur)
			
	strResult = "["
	strInsert = ""
	for ch in aryBuffer:
		strResult = strResult + strInsert + ch
		strInsert = ", "
	
	strResult = strResult + "]"
	
	print "Case #" + str(nCase) + ": " + strResult
	
	