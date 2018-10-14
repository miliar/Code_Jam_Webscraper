import re
from pprint import pprint

fr = open("input.txt", 'r')
fw = open("output.txt", 'w')

lines = fr.readlines()

numTests = lines[0].strip()
curTest = 0
curLine = 1

# hacked together to do small version of the problem with n <= 9 :(
exp = [ 0, 0, 0, 0, 1, 1, 1, 2, 2, 2 ]

def getLine():
	global curLine
	global lines
	curLine += 1
	return lines[curLine-1]
	
def countHigher(pancakeList, val):
	idx = 1
	count = 0
	while idx < len(pancakeList) and pancakeList[idx] >= val:
		count += exp[pancakeList[idx]]
		idx += 1
		
	return count

while curTest < int(numTests):
	numNonEmpty = int(getLine().strip())
	numPancakes = sorted(list(map(int, getLine().strip().split())), reverse=True)
	
	curMin = numPancakes[0]
	numWaits = 0
	
	while numPancakes[0] >= 4:
	
		n = 2
		if numPancakes[0] == 9 and ((len(numPancakes) == 1) or (countHigher(numPancakes, 3) < 2)):
			n = 3
		num1 = int(numPancakes[0] / n)
		num2 = numPancakes[0] - num1
					
		numPancakes[0] = num1
		numPancakes.append(num2)

		numPancakes = sorted(numPancakes, reverse=True)
		numWaits += 1
		
		if (numPancakes[0] + numWaits) < curMin:
			curMin = numPancakes[0] + numWaits
			
	fw.write("Case #%d: %s\n" % (curTest+1, curMin))
	curTest += 1
					
fr.close()
fw.close()