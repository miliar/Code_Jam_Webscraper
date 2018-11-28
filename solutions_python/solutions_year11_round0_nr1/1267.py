import time

f = open("testInput.txt")
out = open("Output.txt","w")
numCases = int(f.readline())
i = 0
while i<numCases:
	blue_buttons = []
	orange_buttons = []
	order = []
	buttons = f.readline()
	numButtons = buttons[0]
	buttons = buttons[1:].strip()
	buttonsList = buttons.split()
	currentList = [];
	for button in buttonsList:
		if button == "O":
			currentList = orange_buttons
			order.append("O")
		elif button == "B":
			currentList = blue_buttons
			order.append("B")
		else:
			currentList.append(int(button))
			
	i=i+1
	blueIndex = 0
	orangeIndex = 0
	bluePos = 0
	orangePos = 0
	sec = 0
	nextColor = 0
	blueWait = False
	orangeWait = False
	while blueIndex < len(blue_buttons) or orangeIndex < len(orange_buttons):
		if order[nextColor] == "O" and orangePos == orange_buttons[orangeIndex]:
			orangeIndex=orangeIndex+1
			nextColor=nextColor+1
			orangeWait = True
		elif order[nextColor] == "B" and bluePos == blue_buttons[blueIndex]:
			blueIndex=blueIndex+1
			nextColor=nextColor+1
			blueWait = True
		if not blueWait and blueIndex < len(blue_buttons):
			if blue_buttons[blueIndex] > bluePos:
				bluePos=bluePos+1
			elif blue_buttons[blueIndex] < bluePos:
				bluePos=bluePos-1
		if not orangeWait and orangeIndex < len(orange_buttons):
			if orange_buttons[orangeIndex] > orangePos:
				orangePos=orangePos+1
			elif orange_buttons[orangeIndex] < orangePos:
				 orangePos=orangePos-1
		blueWait = False
		orangeWait = False

		sec = sec + 1;
	out.write( "Case #" +str(i)+": "+ str(sec-1)+"\n")
