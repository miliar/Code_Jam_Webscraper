testName = 'A'
testName = 'A-small-attempt0'
testName = 'A-small-attempt1'
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

T = int(pop(0))

for t in range(T):
	(R, C) = map(int, pop(0).split())
	Rrange = range(R)
	Crange = range(C)

	tiles = []
	for r in Rrange:
		tiles.append(pop(0))

	stop = False
	skip = False
	for r in Rrange:
		row = tiles[r]
		for c in Crange:
			if skip:
				skip = False
				continue

			tile = row[c]
			if tile == '#':
				if c + 1 == C or row[c+1] != '#' or r+1 == R:
					stop = True
					break

				nextRow = tiles[r+1]
				if nextRow[c] != '#' or nextRow[c+1] != '#':
					stop = True
					break

				row = tiles[r] = row[:c] + '/\\' + row[c+2:]
				tiles[r+1] = nextRow[:c] + '\\/' + nextRow[c+2:]
				skip = True
				#tiles[r+1][c] = '\\'
				#tiles[r+1][c+1] = '/'

		if stop: break

	output += "Case #%d:\n" % (t + 1)
	if stop:
		output += "Impossible\n"
	else:
		for r in Rrange:
			output += tiles[r] + "\n"

#print output

outputFile = open(testName+'.out', 'w')
outputFile.write(output)
outputFile.close()
