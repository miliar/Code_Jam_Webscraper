numCases = int(input())

output = ""

for i in range(1, numCases + 1):
	output += "Case #" + str(i) + ": "

	answer1 = int(input())
	for i in range(answer1 - 1):
		input()

	firstRow = set(input().split())

	for i in range(answer1 - 1, 3):
		input()

	answer2 = int(input())
	for i in range(answer2 - 1):
		input()

	secondRow = set(input().split())

	for i in range(answer2 - 1, 3):
		input()

	intersection = firstRow & secondRow
	if len(intersection) == 1:
		output += intersection.pop()
	elif len(intersection) > 1:
		output += "Bad magician!"
	elif len(intersection) == 0:
		output += "Volunteer cheated!"

	output += "\n"


print(output)
