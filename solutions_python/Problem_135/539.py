import sys 

T = int(sys.stdin.readline())

for tc in range(T):
	answer1 = int(sys.stdin.readline())
	for i in range(answer1):
		line1 = sys.stdin.readline()
	line1 = map(int,(line1).split())

	#skip remaining lines
	for i in range(4 - answer1):
		sys.stdin.readline()

	answer2 = int(sys.stdin.readline())
	for i in range(answer2):
		line2 = sys.stdin.readline()
	line2 = map(int,(line2).split())

	#skip remaining lines
	for i in range(4 - answer2):
		sys.stdin.readline()

	intersection = [val for val in line1 if val in line2]

	if len(intersection) == 0:
		output = 'Volunteer cheated!'
	elif len(intersection) > 1:
		output = 'Bad magician!'
	else:
		output = intersection[0]

	print "Case #" + str(tc + 1) + ": " + str(output)