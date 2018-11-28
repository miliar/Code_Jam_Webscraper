
def cutPancakeLine(pancakeLine):
	while len(pancakeLine) != 0 and pancakeLine[0] == '+':
		pancakeLine = pancakeLine[1:]
	return pancakeLine

def reversePancakeLine(pancakeLine, number):
	tmpNumber = 0
	newPancakeLine = ""
	while tmpNumber < number:
		newPancakeLine += '-' if pancakeLine[tmpNumber] == '+' else '+'
		tmpNumber += 1
	return newPancakeLine + pancakeLine[number:]

def resolvePancakeProblem(pancakeLine, number):
	nbFlip = 0
	pancakeLine = cutPancakeLine(pancakeLine)
	while len(pancakeLine) >= number:
		pancakeLine = reversePancakeLine(pancakeLine, number)
		nbFlip += 1
		pancakeLine = cutPancakeLine(pancakeLine)
	for elem in pancakeLine:
		if elem == '-':
			return "Impossible"
	return nbFlip

nbTest = input()
for i in range(1, nbTest + 1):
	pancakeLine, number = raw_input().split(' ')
	number = int(number)
	print "Case #"+ str(i) + ":", resolvePancakeProblem(pancakeLine, number)