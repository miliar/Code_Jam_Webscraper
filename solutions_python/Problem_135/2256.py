import sys

T = int(sys.stdin.readline())

for i in range(1, T+1):
	q1row = int(sys.stdin.readline())
	for k in range(1, 5):
		row = map(int, sys.stdin.readline().split())
		if k == q1row:
			possibleAns1 = row

	q2row = int(sys.stdin.readline())
	for k in range(1, 5):
		row = map(int, sys.stdin.readline().split())
		if k == q2row:
			possibleAns2 = row

	ans = [val for val in possibleAns1 if val in possibleAns2]
	if len(ans) == 0:
		print "Case #{0}: {1}".format(i, "Volunteer cheated!")
	elif len(ans) > 1:
		print "Case #{0}: {1}".format(i, "Bad magician!")
	else:
		print "Case #{0}: {1}".format(i, ans[0])