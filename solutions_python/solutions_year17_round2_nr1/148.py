import codejam

lines = codejam.input("A")
while len(lines) > 0:
	[D, N] = list(map(int, lines.pop(0).split(" ")))
	max_finish = 0
	for i in range(N):
		[K, S] = list(map(int, lines.pop(0).split(" ")))
		finish = (D - K) / S
		max_finish = max(max_finish, finish)
	codejam.case(D / max_finish)

codejam.finish()