testName = 'C-large-practice'
#testName = 'C-small-attempt0'
#testName = 'C-test'

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
	R = int( params[0] )
	k = int( params[1] )

	groups = map(int, pop(0).split(" "))

	popGroup = groups.pop
	appendGroup = groups.append

	money = 0
	for r in range(R):
		room = k
		riding = []
		appendRiding = riding.append
		while len(groups):
			group = groups[0]
			if room - group >= 0:
				money += group
				room -= group
				popGroup(0)
				appendRiding(group)
			else:
				break
		for g in riding:
			appendGroup(g)
	output += "Case #%d: %s\n" % (t+1, money)

print output

outputFile = open(testName+'.out', 'w')
outputFile.write(output)
outputFile.close()