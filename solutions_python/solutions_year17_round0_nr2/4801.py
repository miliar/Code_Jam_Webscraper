import sys


def ones(num,final):
	out = ""
	for n in range(num):
		out += str(final)
	return int(out)



def isTidy(num):
	numString = str(num)
	for place in range(len(numString)):
		if place > 1 and int(numString[place] < int(numString[0])):
			return False
	for place in range(len(numString)):
		if place > 0 and int(numString[place]) >= int(numString[place-1]):
			pass
		elif place > 0:
			return False
	return True

def solveCase(caseNum, num):
	numLength = len(str(num))
	while not isTidy(num):
		numSet = False
		for n in range(1,int(str(num)[0])+1):
			if num < ones(numLength,n) and not numSet:
				if n != 1:
					num = int(str(n-1) + str(ones(numLength-1,9)))
				else:
					num = ones(numLength-1,9)
				numSet = True
		if not numSet:
			num -= 1
	print "Case #" + str(caseNum) + ": " + str(num)


caseNum = 0
for line in sys.stdin:
	if caseNum > 0:
		solveCase(caseNum, int(line))
	caseNum += 1