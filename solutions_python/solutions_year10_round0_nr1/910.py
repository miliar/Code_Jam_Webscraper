#testName = 'A-large-practice'
testName = 'A-small-attempt0'
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
	params = pop(0).split(" ")
	N = int( params[0] )
	K = int( params[1] )

	snappersOn = [False for i in range(N)]
	snappersPower = [False for i in range(N)]
	snappersPower[0] = True

	for i in range(K):
		for s in range(N):
			if not snappersPower[s]:
				break
			snapperOn = True
			if snappersOn[s] == True:
				snapperOn = False

			snappersOn[s] = snapperOn
		for s in range(1, N):
			if snappersOn[s-1] and snappersPower[s-1]:
				snappersPower[s] = True
			else:
				snappersPower[s] = False

	if snappersPower[-1] and snappersOn[-1]:
		on = "ON"
	else:
		on = "OFF"
	output += "Case #%d: %s\n" % (t+1, on)

print output

outputFile = open(testName+'.out', 'w')
outputFile.write(output)
outputFile.close()
