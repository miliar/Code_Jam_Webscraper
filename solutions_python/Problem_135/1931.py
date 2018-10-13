import sys
f = open(sys.argv[1])
T = int(f.readline().strip())

for t in range(T):
	ans1 = int(f.readline().strip())
	board1 = []
	for i in range(4):
		board1.append(f.readline().strip().split(' '))
	#print board1
	ans2 = int(f.readline().strip())
	board2 = []
	for i in range(4):
		board2.append(f.readline().strip().split(' '))
	#print board2
	ans = set(board1[ans1 - 1]) & set(board2[ans2 - 1])
	if len(ans) == 0:
		guess = "Volunteer cheated!"
	elif len(ans) == 1:
		guess = ans.pop()
	else:
		guess = "Bad magician!"

	print "Case #" + str(t + 1) + ":", guess