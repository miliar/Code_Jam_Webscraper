import collections

T = int(raw_input())

for i in range(0,T):
	firstPick = int(raw_input())
	firstLines = [raw_input().split(), raw_input().split(), raw_input().split(), raw_input().split()]
	secondPick = int(raw_input())
	secondLines = [raw_input().split(), raw_input().split(), raw_input().split(), raw_input().split()]

	firstPossibilities = firstLines[firstPick - 1]
	secondPossibilities = secondLines[secondPick - 1]

	solutions = [x for x, y in collections.Counter(firstPossibilities + secondPossibilities).items() if y > 1]

	if len(solutions) == 1:
		toPrint = solutions[0]
	elif len(solutions) > 1:
		toPrint = "Bad magician!"
	else:
		toPrint = "Volunteer cheated!"

	print "Case #%d: %s" %((i + 1), toPrint)