#testName = 'B'
testName = 'B-small-attempt0'
testName = 'B-small-attempt1'
testName = 'B-small-attempt2'
testName = 'B-large'
#testName = 'B-large'

inputFile = open(testName+'.in', 'r')
input = inputFile.read()
inputFile.close()
del inputFile

output = ""

lines = input.split("\n")
pop = lines.pop
del input

baseElements = 'QWERASDF'

T = int( pop(0) )

for t in range(T):
	chars = pop(0).split(" ")
	popChar = chars.pop

	C = int(popChar(0))
	combinations = {}

	for c in range(C):
		combination = popChar(0)
		combinations[combination[:2]] = combination[2]
		combinations[combination[1]+combination[0]] = combination[2]

	D = int(popChar(0))
	opposing = {}
	for d in range(D):
		oppose = popChar(0)
		opposing[oppose] = 1
		opposing[oppose[1] + oppose[0]] = 1

	N = int(popChar(0))
	toInvoke = popChar(0)
	invoked = ""
	invokedNum = 0
	for c in toInvoke:
		addChar = True

		if invokedNum > 0:
			lastTwo = invoked[-1] + c
			if lastTwo[1] in baseElements:
				if lastTwo[0] in baseElements and combinations.has_key(lastTwo):
					invoked = invoked[:-1] + combinations[lastTwo]
					invokedNum -= 1
					continue
				else:
					for i in invoked:
						if opposing.has_key(i+c):
							invoked = ""
							invokedNum = 0
							addChar = False
							break
		if addChar:
			invoked += c
			invokedNum += 1


	outStr = "["
	if len(invoked) > 0:
		for i in invoked: outStr += i + ", "
		outStr = outStr[:-2]

	output += "Case #%d: %s\n" % (t+1, outStr + "]")
	#if t == 3: break

print output

outputFile = open(testName+'.out', 'w')
outputFile.write(output)
outputFile.close()
