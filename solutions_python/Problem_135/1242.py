with open('A-small-attempt2.in') as fin:
	content = fin.readlines()
n = int(content[0])
content = content[1:]
output = ""

for j in range(n):
	firstRow = int(content[0])
	content = content[1:]

	for i in range(4):
		line = content[0]
		content = content[1:]
		if i + 1 == firstRow:
			firstPossibles = set(line.split())

	secondRow = int(content[0])
	content = content[1:]

	for i in range(4):
		line = content[0]
		content = content[1:]
		if i + 1 == secondRow:
			secondPossibles = set(line.split())

	result = firstPossibles.intersection(secondPossibles)

	if len(result) == 1:
		output += "Case #" + `j + 1` + ": " + result.pop() + "\n"
	elif len(result) > 1:
		output += "Case #" + `j + 1` + ": Bad magician!\n"
	else:
		output += "Case #" + `j + 1` + ": Volunteer cheated!\n"

f = open('magicTrickOut.txt', 'w')
f.write(output)
f.close()