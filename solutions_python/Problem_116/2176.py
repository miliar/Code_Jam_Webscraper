def tictactoe (game):
	for i in range(0,4):
		if game[i][0]==game[i][1]:
			if game[i][2]==game[i][3]:
				if game[i][1]==game[i][2]:
					if game[i][0]!='.':
						return game[i][0]
	for j in range(0,4):
			if game[0][j]==game[1][j]:
				if game[2][j]==game[3][j]:
					if game[1][j]==game[2][j]:
						if game[0][j]!='.':
							return game[0][j]
	
	if game[0][0]==game[1][1]:
			if game[2][2]==game[3][3]:
				if game[1][1]==game[2][2]:
					if game[0][0]!='.':
						return game[0][0]	
							
	if game[0][3]==game[1][2]:
			if game[2][1]==game[3][0]:
				if game[1][2]==game[3][0]:
					if game[0][3]!='.':
						return game[0][3]
	
	for i in range(0,4):
		for j in range(0,4):
			if game[i][j]==".":
				return "Game has not completed"
	return "Draw"
	
def entermatrix(entered,T):
	for i in range(0,4):
		if entered[i]=="T":
			entered[i]=T
	return entered
	
numcases=int(raw_input("number of cases"))
answers=[]

for i in range(0,numcases):
	ticarray1=[0,0,0,0]
	ticarray2=[0,0,0,0]
	
	firstrow=list(raw_input())
	firstrow1=firstrow[:]
	ticarray1[0]=entermatrix(firstrow,"O")	
	ticarray2[0]=entermatrix(firstrow1,"X")	
	
	secondrow=list(raw_input())
	secondrow1=secondrow[:]
	ticarray1[1]=entermatrix(secondrow,"O")
	ticarray2[1]=entermatrix(secondrow1,"X")
	
	thirdrow=list(raw_input())
	thirdrow1=thirdrow[:]
	ticarray1[2]=entermatrix(thirdrow,"O")
	ticarray2[2]=entermatrix(thirdrow1,"X")
	
	fourthrow=list(raw_input())
	fourthrow1=fourthrow[:]
	ticarray1[3]=entermatrix(fourthrow,"O")
	ticarray2[3]=entermatrix(fourthrow1,"X")
		
	answer1=tictactoe(ticarray1)
	answer2=tictactoe(ticarray2)
	
	if len(answer1)==1:
		answers.append(answer1)
	elif len(answer2)==1:
		answers.append(answer2)
	elif len(answer1)<=len(answer2):
		answers.append(answer1)
	else:
		answers.append(answer2)
		
	raw_input()
	
for i in range(0,numcases):
	if len(answers[i])==1:
		
		print "Case #%s: %s won" % (i+1,answers[i])
	else:
		
		print "Case #%s: %s" % (i+1,answers[i])
	

























