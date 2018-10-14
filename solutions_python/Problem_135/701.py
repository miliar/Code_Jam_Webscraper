f = open("A-small-attempt0.in", "r")

output = open("pa_test.out", "w")

T = int(f.readline().rstrip("\n"))

for round in range(1, T+1):
	answer1 = int(f.readline().rstrip("\n"))
	row1 = []
	for i in range(1, 5):
		if i == answer1:
			row1 = f.readline().rstrip("\n").split(" ")
		else:
			f.readline()

	answer2 = int(f.readline().rstrip("\n"))
	row2 = []
	for i in range(1, 5):
		if i == answer2:
			row2 = f.readline().rstrip("\n").split(" ")
		else:
			f.readline()

	intersection = [x for x in row1 if x in row2]

	if len(intersection) == 0:

		output.write("Case #%d: Volunteer cheated!\n" % round)
	elif len(intersection) == 1:
		output.write("Case #%d: %d\n" % (round, int(intersection[0])))
	else:
		output.write("Case #%d: Bad magician!\n" % round)
	