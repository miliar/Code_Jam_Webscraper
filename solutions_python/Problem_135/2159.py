
def process(arrangement1, arrangement2, guess1, guess2):
	arr1 = arrangement1[guess1-1]
	arr2 = arrangement2[guess2-1]	
	for elem in arr2:
		if elem in arr1:
			break
	else:
		return "Volunteer cheated!"
	count = 0	
	for elem in arr2:
		if elem in arr1:
			correctGuess = elem
			count+=1
	
	if count > 1:
		return "Bad magician!"

	return str(correctGuess)
	
	

noTestCases = int(raw_input())
caseNo = 0
while(noTestCases > 0):
	caseNo +=1
	guess1 = int(raw_input())
	arrangement1 = []
	for i in range(4):
		row = raw_input()
		row = row.split()
		row = [int(elem) for elem in row]
		arrangement1.append(row)	
	guess2 = int(raw_input())
	arrangement2 = []
	for i in range(4):
		row = raw_input()
		row = row.split()
		row = [int(elem) for elem in row]
		arrangement2.append(row)
	op = process(arrangement1, arrangement2, guess1, guess2)
	print "case #%d: %s" %(caseNo, op)
	noTestCases -= 1