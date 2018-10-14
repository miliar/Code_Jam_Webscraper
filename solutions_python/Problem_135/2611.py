import sys

def readBoard():
	ans = int(sys.stdin.readline().strip())
	rows = []
	for i in range(4):
		rows.append(sys.stdin.readline().strip())
	return rows, ans
	
def findAnswer(row1, row2):
	firstrow = [int(x) for x in row1.split()]
	secondrow = [int(x) for x in row2.split()]
	ans = []
	#Not efficient...
	for e in firstrow:
		if e in secondrow:
			ans.append(e)
	if len(ans) == 0:
		print "Volunteer cheated!"
	elif len(ans) > 1:
		print "Bad magician!"
	else:
		print ans[0]
		
def handleTestCase(nr):
	print "Case #"+str(nr)+":",
	board1, ans1 = readBoard()
	board2, ans2 = readBoard()
	findAnswer(board1[ans1-1], board2[ans2-1])

nrC = int(sys.stdin.readline().strip())
for i in range(1, nrC+1):
	handleTestCase(i)
