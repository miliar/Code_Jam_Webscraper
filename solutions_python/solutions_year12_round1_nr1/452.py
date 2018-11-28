#passwordprob.py

ENTER_COST = 1
BACK_COST = 1

cases = int(raw_input())
for caseNo in range(cases):
	typed, totalChars = raw_input().split()
	typed = int(typed)
	totalChars = int(totalChars)
	charChance = raw_input().split()
	for i in range(len(charChance)):
		charChance[i] = float(charChance[i])
	
	noErrors = charChance[0]
	for charProb in range(1,typed):
		noErrors *= charChance[charProb]
	noErrorsExpected = (noErrors * (totalChars - typed + ENTER_COST)) + ((1 - noErrors) * ((totalChars - typed + ENTER_COST) + (totalChars + 1)))
	enterInstantExpected = (ENTER_COST + totalChars + ENTER_COST)
	curBest = min(noErrorsExpected, enterInstantExpected)
	exChances = []
	for backSpaces in range(typed):
		if backSpaces == 0:
			continue
		if typed == 3:
			poss = []
			poss.append(charChance[0] * charChance[1] * charChance[2])
			pStrk1 = (BACK_COST * backSpaces) + backSpaces + (totalChars - typed) + ENTER_COST
			poss.append(charChance[0] * charChance[1] * (1 - charChance[2]))
			pStrk2 = (BACK_COST * backSpaces) + backSpaces + (totalChars - typed) + ENTER_COST
			poss.append(charChance[0] * (1 - charChance[1]) *  charChance[2])
			pStrk3 = (BACK_COST * backSpaces) + backSpaces + (totalChars - typed) + ENTER_COST
			if backSpaces == 1:
				pStrk3 += totalChars + ENTER_COST
			poss.append((1 - charChance[0]) * charChance[1] * charChance[2])
			pStrk4 = (BACK_COST * backSpaces) + backSpaces + (totalChars - typed) + ENTER_COST
			if backSpaces < 3:
				pStrk4 += totalChars + ENTER_COST
			poss.append(charChance[0] * (1 - charChance[1]) * (1 - charChance[2]))
			pStrk5 = (BACK_COST * backSpaces) + backSpaces + (totalChars - typed) + ENTER_COST
			if backSpaces == 1:
				pStrk5 += totalChars + ENTER_COST
			poss.append((1 - charChance[0]) * (1 - charChance[1]) * charChance[2])
			pStrk6 = (BACK_COST * backSpaces) + backSpaces + (totalChars - typed) + ENTER_COST
			if backSpaces < 3:
				pStrk6 += totalChars + ENTER_COST
			poss.append((1 - charChance[0]) * charChance[1] * (1 - charChance[2]))
			pStrk7 = (BACK_COST * backSpaces) + backSpaces + (totalChars - typed) + ENTER_COST
			if backSpaces < 3:
				pStrk7 += totalChars + ENTER_COST
			poss.append((1 - charChance[0]) * (1 - charChance[1]) * (1 - charChance[2]))
			pStrk8 = (BACK_COST * backSpaces) + backSpaces + (totalChars - typed) + ENTER_COST + totalChars + ENTER_COST
			
			if ((pStrk1 * poss[0]) + (pStrk2 * poss[1]) + (pStrk3 * poss[2]) + (pStrk4 * poss[3]) + (pStrk5 * poss[4]) + (pStrk6 * poss[5]) + (pStrk7 * poss[6]) + (pStrk8 * poss[7])) < curBest:
				curBest = ((pStrk1 * poss[0]) + (pStrk2 * poss[1]) + (pStrk3 * poss[2]) + (pStrk4 * poss[3]) + (pStrk5 * poss[4]) + (pStrk6 * poss[5]) + (pStrk7 * poss[6]) + (pStrk8 * poss[7]))
				
		elif typed == 2:
			poss = []
			poss.append(charChance[0] * charChance[1])
			pStrk1 = (BACK_COST * backSpaces) + backSpaces + (totalChars - typed) + ENTER_COST
			poss.append((1 - charChance[0]) * charChance[1])
			pStrk2 = (BACK_COST * backSpaces) + backSpaces + (totalChars - typed) + ENTER_COST + totalChars + ENTER_COST
			poss.append(charChance[0] * (1 - charChance[1]))
			pStrk3 = (BACK_COST * backSpaces) + backSpaces + (totalChars - typed) + ENTER_COST
			poss.append((1 - charChance[0]) * (1 - charChance[1]))
			pStrk4 = (BACK_COST * backSpaces) + backSpaces + (totalChars - typed) + ENTER_COST + totalChars + ENTER_COST
			
			if (pStrk1 * poss[0]) + (pStrk2 * poss[1]) + (pStrk3 * poss[2]) + (pStrk4 * poss[3]) < curBest:
				curBest = (pStrk1 * poss[0]) + (pStrk2 * poss[1]) + (pStrk3 * poss[2]) + (pStrk4 * poss[3])
			
				
				
		elif typed == 1:
			poss = []
			poss.append(charChance[0])
			pStrk1 = (BACK_COST * backSpaces) + backSpaces + (totalChars - typed) + ENTER_COST
			poss.append(1 - charChance[0])
			pStrk2 = (BACK_COST * backSpaces) + backSpaces + (totalChars - typed) + ENTER_COST + totalChars + ENTER_COST
			
			if (pStrk1 * poss[0]) + (pStrk2 * poss[1]) < curBest:
				curBest = (pStrk1 * poss[0]) + (pStrk2 * poss[1])
			
			
	
	print "Case #%i: %f" % (caseNo+1, curBest)