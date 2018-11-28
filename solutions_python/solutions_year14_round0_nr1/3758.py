#!python

def out_put(case, answer):
	print "Case #" + str(case) + ": " + answer

N = int(raw_input())
for i in xrange(0, N):
	fr = int(raw_input())
	board = []
	for j in xrange(0, 4):
		board.append(raw_input().split())
	counter = {}
	for item in board[fr - 1]:
		counter[item] = True

	for item in counter:
		counter[item] = False

	board = []
	sr = int(raw_input())
	for j in xrange(0, 4):
		board.append(raw_input().split())

	for item in board[sr - 1]:
		if item in counter:
			counter[item] = True

	num_same = 0
	unique = None
	for item in counter:
		if counter[item]:
			num_same += 1
			unique = item

	if num_same == 0:
		out_put(i + 1, "Volunteer cheated!")
	elif num_same == 1:
		out_put(i + 1, unique)
	else:
		out_put(i + 1, "Bad magician!")
