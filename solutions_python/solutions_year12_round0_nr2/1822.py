
def getResult(inStr):
	data = inStr.split(' ')
	maxNumSuprisingScores = int(data[1])
	requesrdBestJudgeResult = int(data[2])
	
	contestentsTotal = data[3:]
	
	nonSuprisingPasses = 0
	SuprisingPasses = 0
	
	for strConTotal in contestentsTotal:
		if strConTotal:
			conTotal = int(strConTotal)
			adv = conTotal/3
			bestNonSprisisngScore = adv
			# check if a non suprising score passes
			
			# case 3, best (1,1,1), so adv
			# case 4, best (1,1,2), so adv+1
			# case 5, best (1,2,2), so adv+1 
			if conTotal%3 != 0:
				bestNonSprisisngScore += 1
			
			#clip off at 10
			if bestNonSprisisngScore > 10:
				bestNonSprisisngScore = 10
			
			if bestNonSprisisngScore >= requesrdBestJudgeResult:
				nonSuprisingPasses += 1
			else:
				# check if a suprising score passes
				
				# case 3, best (0,1,2), so adv+1
				# case 4, best (0,2,2), so adv+1
				# case 5, best (1,1,3), so adv+2 
				if conTotal%3 == 0:
					bestSprisisngScore = adv + 1
				elif conTotal%3 == 1:
					bestSprisisngScore = adv + 1
				else:
					bestSprisisngScore = adv + 2
				
				# clip off at 0
				if adv <= 0:
					# only possiable score (0,0,0)
					bestSprisisngScore = 0
				
				# clip off at 10
				if bestSprisisngScore > 10:
					bestSprisisngScore = 10
				
				if bestSprisisngScore >= requesrdBestJudgeResult:
					SuprisingPasses += 1
		
	return nonSuprisingPasses + min(SuprisingPasses, maxNumSuprisingScores)
		

#how many lines are we reading?
num = int(raw_input())

for i in range(0, num):
	print 'Case #'+str(i+1)+': '+str(getResult(raw_input()))