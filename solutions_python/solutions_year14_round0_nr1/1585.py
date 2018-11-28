import sys

num_cases = int(sys.stdin.readline().strip())

def get_state():
	answer = int(sys.stdin.readline().strip())
	board = [map(int, sys.stdin.readline().strip().split()) for row_num in range(0, 4)]
	return answer, board
	
for i in range(num_cases):
	answer1, board1 = get_state()
	row1 = board1[answer1-1]
	# print answer1, board1, row1
	answer2, board2 = get_state()
	row2 = board2[answer2-1]
	# print answer2, board2, row2
	intersect = set(row1).intersection(row2)
	if not intersect:
		result = "Volunteer cheated!"
	elif len(intersect) == 1:
		result = list(intersect)[0]
	else:
		result = "Bad magician!"
	print "Case #%s: %s" % (i+1, result)