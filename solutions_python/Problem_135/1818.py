import sys, math

cases = int(sys.stdin.readline().rstrip())

for case in range(cases):

	first_answer = int(sys.stdin.readline().rstrip())

	first_configuration = []
	
	for i in range(4):

		row = map(int, sys.stdin.readline().rstrip().split())

		first_configuration.append(row)

	second_answer = int(sys.stdin.readline().rstrip())

	second_configuration = []

	for i in range(4):

		row = map(int, sys.stdin.readline().rstrip().split())

		second_configuration.append(row)

	result = set(first_configuration[first_answer-1]).intersection(set(second_configuration[second_answer-1]))

	if len(result) == 1:

		text = result.pop()

	elif len(result) > 1:

		text = 'Bad magician!'

	elif len(result) == 0:

		text = 'Volunteer cheated!'

	print 'Case #' + str(case + 1) + ': ' + str(text)
