from sys import stdin
f = open('output.out', 'w')

for i in range(int(stdin.readline())):
	lineread = stdin.readline().split()
	dancers = int(lineread[0])
	surprises = int(lineread[1])
	maxScore = int(lineread[2])
	
	dancersWithAtLeastMaxScore = 0
	for j in range(3,len(lineread)):
		totalScore = int(lineread[j])
		lowestScore1 = maxScore-1 if maxScore-1 >= 0 else 0
		lowestScore2 = maxScore-2 if maxScore-2 >= 0 else 0
		if (maxScore + 2*(lowestScore1)) <= totalScore:
			dancersWithAtLeastMaxScore += 1
		elif (maxScore + 2*(lowestScore2)) <= totalScore\
			and surprises > 0:				
				dancersWithAtLeastMaxScore += 1
				surprises -= 1
			
	print 'Case #'+str(i+1)+': ' + str(dancersWithAtLeastMaxScore)
	f.write('Case #'+str(i+1)+': ' + str(dancersWithAtLeastMaxScore) + '\n')

f.close()
