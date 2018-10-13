import sys

test_count = int(sys.stdin.readline())

for test_id in range(1, test_count + 1):
	answer1 = int(sys.stdin.readline())
	for row in range(1, 5):
		row_str = sys.stdin.readline().strip()
		if row == answer1:
			candidates1 = set(map(int, row_str.split(' ')))
	answer2 = int(sys.stdin.readline())
	for row in range(1, 5):
		row_str = sys.stdin.readline().strip()
		if row == answer2:
			candidates2 = set(map(int, row_str.split(' ')))
	solution = candidates1.intersection(candidates2)
	if len(solution) == 0:
		solution_msg = 'Volunteer cheated!'
	elif len(solution) == 1:
		solution_msg = str(list(solution)[0])
	else:
		solution_msg = 'Bad magician!'
	print('Case #%d: %s' % (test_id, solution_msg))
