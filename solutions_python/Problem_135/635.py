def solve(board1, board2, r1, r2):
	res = []
	for n in board2[r2]:
		if n in board1[r1]:
			res.append(n)
	if len(res) == 1:
		return res[0]
	elif len(res) > 1:
		return "Bad magician!"
	else:
		return "Volunteer cheated!"

for t in range(int(input())):
	r1 = int(input()) - 1
	board1 = [ [int(s) for s in input().split(" ")] for _ in range(4)]
	r2 = int(input()) - 1
	board2 = [ [int(s) for s in input().split(" ")] for _ in range(4)]
	print("Case #" + str(t+1) + ": " + str(solve(board1, board2, r1, r2)))
