f = open('data.in')
lines = f.readlines()
f.close()

lines = [lines.rstrip('\n') for lines in open('data.in')]

testNumber = int(lines[0])
n = 0
userInput = 0
lineNumber = 1
temp1 = []
temp2 = []

o = open('out.in','w')
while(n < testNumber):
	userInput = int(lines[lineNumber])
	temp1 = lines[lineNumber + userInput].split()
	lineNumber+=5
	userInput = int(lines[lineNumber])
	temp2 = lines[lineNumber + userInput].split()
	lineNumber+=5
	
	counter = 0
	for card1 in temp1:
		for card2 in temp2:
			if(int(card1) == int(card2)):
				theCard = card1
				counter+=1

	if(counter == 0):
		o.write("Case #%s:" % str(n+1) + " Volunteer cheated!\n")

	elif(counter == 1):
		o.write("Case #%s:" % str(n+1) + " " + theCard + "\n")
	else:
		o.write("Case #%s:" % str(n+1) + " Bad Magician!\n")
	n+=1

f.close()