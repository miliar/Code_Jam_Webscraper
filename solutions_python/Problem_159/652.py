from sys import stdin, stdout

T = int(stdin.readline())

for t in range(T):
	stdin.readline()
	amounts = map(int, stdin.readline().strip().split())

	eatenAbs = 0
	eaternRate = 0
	
	for a in range(len(amounts) - 1):
		#amounts[a] amounts[a + 1]

		eatenAbs += max(0, amounts[a] - amounts[a + 1])

		eaternRate = max(eaternRate, amounts[a] - amounts[a + 1])

	eaternGrad = 0
	for a in range(len(amounts) - 1):
		eaternGrad += min(eaternRate, amounts[a])

	stdout.write("Case #%d: %d %d\n"%(t+1, eatenAbs, eaternGrad))