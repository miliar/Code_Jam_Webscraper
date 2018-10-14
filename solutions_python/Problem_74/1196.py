file = open("A-large.in")
results = open("results", 'w')

numberOfTests = int(file.readline().strip("\n"))

for i in range(0, numberOfTests):
	data = file.readline().strip("\n")
	
	dataList = data.split(" ")
	
	presses = int(dataList.pop(0))
	
	moves = []
	
	for x in range(0, presses):
		robot = dataList.pop(0)
		button = int(dataList.pop(0))
			
		moves.append((robot, button))
	
	print moves
	
	orangePos = 1
	bluePos = 1 
	
	t = 0
	
	while 1:
		
		t+= 1
		
		popFront = 0
		
		cM = moves[0]
		
		if (cM[0] == "O"):
			if orangePos == cM[1]:
				popFront = 1
			elif orangePos > cM[1]:
				orangePos -= 1
			elif orangePos < cM[1]:
				orangePos += 1
				
			for move in moves:
				if move[0] == "B":
					if bluePos > move[1]:
						bluePos -= 1
					elif bluePos < move[1]:
						bluePos += 1
					break
					
		else:
			if bluePos == cM[1]:
				popFront = 1
			elif bluePos > cM[1]:
				bluePos -= 1
			elif bluePos < cM[1]:
				bluePos += 1
				
			for move in moves:
				if move[0] == "O":
					if orangePos > move[1]:
						orangePos -= 1
					elif orangePos < move[1]:
						orangePos += 1
					break
			
		
		if (popFront):
			popFront = 0
			moves.pop(0)
			
		if (len(moves) == 0):
			print t
			results.write("Case #")
			results.write(str(i + 1))
			results.write(": ")
			results.write(str(t))
			results.write("\n")
			break
			
	
			
file.close()
results.close()