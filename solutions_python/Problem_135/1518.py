import sys

def solve(g1, board1, g2, board2):
	answer = set(board1[g1-1]) & set(board2[g2-1])
	if len(answer) == 1:
		return answer.pop()
	if len(answer) > 1:
		return "Bad magician!"
	if len(answer) == 0:
		return "Volunteer cheated!"



T = int(sys.stdin.readline())
for i in range(T):
	g1 = int(sys.stdin.readline())
	board1 = []
	for _ in range(4):
		board1.append(map(int, sys.stdin.readline().split(' ')))
	g2 = int(sys.stdin.readline())
	board2 = []
	for _ in range(4):
		board2.append(map(int, sys.stdin.readline().split(' ')))
	print "Case #{0}: {1}".format(i+1, solve(g1, board1, g2, board2))
