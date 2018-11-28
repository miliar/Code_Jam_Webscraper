import sys
C = int(sys.stdin.readline())
for testcase in range(1, C + 1):
	(N, K, B, T) = map(int, sys.stdin.readline().split())
	X = list(map(int, sys.stdin.readline().split()))
	V = list(map(int, sys.stdin.readline().split()))
	elect = [X[chick] + V[chick] * T >= B for chick in range(N)]
	if sum(elect) < K:
		print('Case #%d: IMPOSSIBLE' % testcase)
	else:
		n_saved = 0
		n_overtaken = 0
		count = 0
		while len(elect) and elect[-1]:
			elect.pop()
			n_saved += 1
		index = -1
		while n_saved < K:
			if elect[index]:
				n_saved += 1
				count += n_overtaken
			else:
				n_overtaken += 1
			index -= 1
		print('Case #%d: %d' % (testcase, count))