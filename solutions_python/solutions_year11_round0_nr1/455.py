buttonPos = {}
buttonColors = []
botPos = {}

def initCase(words):
	del words[0]
	buttonPos.clear()
	del buttonColors[:]
	botPos.clear()

	for i in range(0, len(words), 2):
		buttonColors.append(words[i])
		if words[i] in buttonPos:
			buttonPos[words[i]].append(int(words[i+1]))
		else:
			buttonPos[words[i]] = [int(words[i+1])]
			
	for key in buttonPos:
		botPos[key] = 1

def solveCase():
	steps = 0
	while len(buttonColors) > 0:
		pushed = 0
		for i in botPos:
			if len(buttonPos[i]) > 0:
				if botPos[i] == buttonPos[i][0] and buttonColors[0] == i and pushed != 1:
					del buttonPos[i][0]
					del buttonColors[0]
					pushed = 1
				elif botPos[i] < buttonPos[i][0]:
					botPos[i] += 1
				elif botPos[i] > buttonPos[i][0]:
					botPos[i] -= 1
		steps += 1
	return steps
	
fileIn = open("A-large.in", "r")
fileOut = open("A-large.out", "w")

num = 0
for line in fileIn:
	if num != 0:
		words = line.strip().split(" ")
		initCase(words)
		fileOut.write("Case #" + str(num) + ": " + str(solveCase()) + "\n")
	num += 1
	
fileIn.close()
fileOut.close()