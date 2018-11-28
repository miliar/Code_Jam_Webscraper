f = open('testinput.in', 'r')
numcases = int(f.readline())
#print numcases
#print "Number of Cases: "+str(numcases)
for i in range(numcases):
	ar = []
	ar.append(f.readline())
	ar.append(f.readline())
	ar.append(f.readline())
	ar.append(f.readline())
	positionOne = ar[0][0]
	winner = ""
	draw = True
	#horizontal
	if((ar[0][0] == "X" or ar[0][0] == "T") and  (ar[0][1] == "X" or ar[0][1] == "T") and (ar[0][2] == "X" or ar[0][2] == "T") and (ar[0][3] == "X" or ar[0][3] == "T")):
		winner = "X"
	#vertical column 1
	if((ar[0][0] == "X" or ar[0][0] == "T") and  (ar[1][0] == "X" or ar[1][0] == "T") and (ar[2][0] == "X" or ar[2][0] == "T") and (ar[3][0] == "X" or ar[3][0] == "T")):
		winner = "X"
	#diag top left to bottom right
	if((ar[0][0] == "X" or ar[0][0] == "T") and  (ar[1][1] == "X" or ar[1][1] == "T") and (ar[2][2] == "X" or ar[2][2] == "T") and (ar[3][3] == "X" or ar[3][3] == "T")):
		winner = "X"
	#diag top right to bottom left
	if((ar[0][3] == "X" or ar[0][3] == "T") and  (ar[1][2] == "X" or ar[1][2] == "T") and (ar[2][1] == "X" or ar[2][1] == "T") and (ar[0][3] == "X" or ar[0][3] == "T")):
		winner = "X"
	#column 2 
	if((ar[0][1] == "X" or ar[0][1] == "T") and  (ar[1][1] == "X" or ar[1][1] == "T") and (ar[2][1] == "X" or ar[2][1] == "T") and (ar[3][1] == "X" or ar[3][1] == "T")):
		winner = "X"
	#column 3
	if((ar[0][2] == "X" or ar[0][2] == "T") and  (ar[1][2] == "X" or ar[1][2] == "T") and (ar[2][2] == "X" or ar[2][2] == "T") and (ar[3][2] == "X" or ar[3][2] == "T")):
		winner = "X"
	#column 4
	if((ar[0][3] == "X" or ar[0][3] == "T") and  (ar[1][3] == "X" or ar[1][3] == "T") and (ar[2][3] == "X" or ar[2][3] == "T") and (ar[3][3] == "X" or ar[3][3] == "T")):
		winner = "X"
	if((ar[1][1] == "X" or ar[1][1] == "T") and  (ar[1][2] == "X" or ar[1][2] == "T") and (ar[1][3] == "X" or ar[1][3] == "T") and (ar[1][0] == "X" or ar[1][0] == "T")):
		winner = "X"
	if((ar[2][0] == "X" or ar[2][0] == "T") and  (ar[2][1] == "X" or ar[2][1] == "T") and (ar[2][2] == "X" or ar[2][2] == "T") and (ar[2][3] == "X" or ar[2][3] == "T")):
		winner = "X"
	if((ar[3][0] == "X" or ar[3][0] == "T") and  (ar[3][1] == "X" or ar[3][1] == "T") and (ar[3][2] == "X" or ar[3][2] == "T") and (ar[3][3] == "X" or ar[3][3] == "T")):
		winner = "X"
	
	if((ar[0][0] == "O" or ar[0][0] == "T") and  (ar[0][1] == "O" or ar[0][1] == "T") and (ar[0][2] == "O" or ar[0][2] == "T") and (ar[0][3] == "O" or ar[0][3] == "T")):
		winner = "O"
	if((ar[0][0] == "O" or ar[0][0] == "T") and  (ar[1][0] == "O" or ar[1][0] == "T") and (ar[2][0] == "O" or ar[2][0] == "T") and (ar[3][0] == "O" or ar[3][0] == "T")):
		winner = "O"
	if((ar[0][0] == "O" or ar[0][0] == "T") and  (ar[1][1] == "O" or ar[1][1] == "T") and (ar[2][2] == "O" or ar[2][2] == "T") and (ar[3][3] == "O" or ar[3][3] == "T")):
		winner = "O"
	if((ar[0][3] == "O" or ar[0][3] == "T") and  (ar[1][2] == "O" or ar[1][2] == "T") and (ar[2][1] == "O" or ar[2][1] == "T") and (ar[0][3] == "O" or ar[0][3] == "T")):
		winner = "O"
	if((ar[1][0] == "O" or ar[1][0] == "T") and  (ar[1][1] == "O" or ar[1][1] == "T") and (ar[1][2] == "O" or ar[1][2] == "T") and (ar[1][3] == "O" or ar[1][3] == "T")):
		winner = "O"
	if((ar[2][0] == "O" or ar[2][0] == "T") and  (ar[2][1] == "O" or ar[2][1] == "T") and (ar[2][2] == "O" or ar[2][2] == "T") and (ar[2][3] == "O" or ar[2][3] == "T")):
		winner = "O"
	if((ar[3][0] == "O" or ar[3][0] == "T") and  (ar[3][1] == "O" or ar[3][1] == "T") and (ar[3][2] == "O" or ar[3][2] == "T") and (ar[3][3] == "O" or ar[3][3] == "T")):
		winner = "O"
	#column 2 
	if((ar[0][1] == "O" or ar[0][1] == "T") and  (ar[1][1] == "O" or ar[1][1] == "T") and (ar[2][1] == "O" or ar[2][1] == "T") and (ar[3][1] == "O" or ar[3][1] == "T")):
		winner = "O"
	#column 3
	if((ar[0][2] == "O" or ar[0][2] == "T") and  (ar[1][2] == "O" or ar[1][2] == "T") and (ar[2][2] == "O" or ar[2][2] == "T") and (ar[3][2] == "O" or ar[3][2] == "T")):
		winner = "O"
	#column 4
	if((ar[0][3] == "O" or ar[0][3] == "T") and  (ar[1][3] == "O" or ar[1][3] == "T") and (ar[2][3] == "O" or ar[2][3] == "T") and (ar[3][3] == "O" or ar[3][3] == "T")):
		winner = "O"

	#print "Winner is " + str(winner)
	if winner == "":
		for z in range(4):
			if ar[z][0] == ".":
				draw = False
			if ar[z][1] == ".":
				draw = False
			if ar[z][2] == ".":
				draw = False
			if ar[z][3] == ".":
				draw = False

	#print "Draw"+str(draw)
	if draw == True and winner == "":
		print "Case #"+str(i+1)+": Draw"
	elif winner == "":
		print "Case #"+str(i+1)+": Game has not completed"
	else:
		print "Case #"+str(i+1)+": "+winner+" won"
	#print ar[0][0]
	f.readline()
	
	
	