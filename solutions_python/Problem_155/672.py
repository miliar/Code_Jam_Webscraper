import fileinput


def solve(shyest, people):
	standing = 0
	stooges = 0
	shyest = int(shyest)
	for shyness in range(0, shyest+1):
		persons = int(people[shyness])
		if (standing>=shyness):
			standing += persons
		elif(persons>0):
			stooges += shyness-standing
			standing += persons +stooges
	return stooges

lines = fileinput.input()

cases = int(lines[0])

for i in range(1, cases+1):
	print("Case #", end="")
	print(i, end="")
	print(": ", end="")
	line = lines[i]
	shyest = line[0]
	shyness = line[2:]
	print(solve(shyest, shyness))

