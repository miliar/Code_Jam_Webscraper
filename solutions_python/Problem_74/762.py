testName = 'A'
testName = 'A-small-attempt0'
testName = 'A-large'
#testName = 'A-test'

inputFile = open(testName+'.in', 'r')
input = inputFile.read()
inputFile.close()
del inputFile

output = ""

lines = input.split("\n")
pop = lines.pop
del input

T = int( pop(0) )

for t in range(T):
	chars = pop(0).split(" ")
	popChar = chars.pop
	N = int(popChar(0))

	commands = []
	popCommand = commands.pop
	for n in range(N):
		commands.append((popChar(0), int(popChar(0))))

	time = 0
	oPos = 1
	bPos = 1

	while len(commands) != 0:
		fCommand = commands[0]
		nCommand = False
		for c in commands:
			if c[0] != fCommand[0]:
				nCommand = c
				break

		if fCommand[0] == 'O':
			#if t == 0: print "first: ", fCommand[1], oPos
			if fCommand[1] != oPos:
				if fCommand[1] > oPos: oPos += 1
				else: oPos -= 1
			else:
				popCommand(0)
		else:
			#if t == 0: print "first: ", fCommand[1], bPos
			if fCommand[1] != bPos:
				if fCommand[1] > bPos: bPos += 1
				else: bPos -= 1
			else:
				popCommand(0)

		
		if nCommand:
			if nCommand[0] == 'O':
				#if t == 0: print "second: ", nCommand, nCommand[1], oPos
				if nCommand[1] != oPos:
					if nCommand[1] > oPos: oPos += 1
					else: oPos -= 1
			else:
				#if t == 0: print "second: ", nCommand, nCommand[1], bPos
				if nCommand[1] != bPos:
					if nCommand[1] > bPos: bPos += 1
					else: bPos -= 1
		time += 1
 

	output += "Case #%d: %s\n" % (t+1, time)

print output

outputFile = open(testName+'.out', 'w')
outputFile.write(output)
outputFile.close()
