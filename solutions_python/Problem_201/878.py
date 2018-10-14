from sys import stdin


def proper(N, K):
	spaces = {N:1}
	nPeople = 0

	while True:
		nSpaces = sum(spaces[key] for key in spaces)
		if nPeople + nSpaces >= K:
			break
		nPeople += nSpaces
		newSpaces = dict()
		for key in spaces:
			count = spaces[key]

			newKey1 = (key - 1) / 2
			newKey2 = (key - 1 + 1) / 2

			if not newKey1 in newSpaces:
				newSpaces[newKey1] = 0
			if not newKey2 in newSpaces:
				newSpaces[newKey2] = 0

			newSpaces[newKey1] += count
			newSpaces[newKey2] += count

		spaces = newSpaces


	for key in sorted(spaces.keys(), reverse=True):
		count = spaces[key]
		nPeople += count
		if nPeople >= K:
			newKey1 = (key - 1) / 2
			newKey2 = (key - 1 + 1) / 2
			return (newKey1, newKey2)

	return (None, None)

def improper(N, K):
	spaces = [N]
	for nPeople in range(K-1):
		key = spaces.pop()
		newKey1 = (key - 1) / 2
		newKey2 = (key - 1 + 1) / 2

		spaces.extend([newKey1, newKey2])
		spaces.sort()

	key = spaces.pop()
	newKey1 = (key - 1) / 2
	newKey2 = (key - 1 + 1) / 2
	return (newKey1, newKey2)

def test(maxN):
	for N in range(2,maxN):
		for K in [N/1, N/2, N/3, N/4, N/5, N/6]:
			if K == 0:
				break
			assert proper(N,K) == improper(N,K)




T = int(stdin.readline())

for caseNum in range(T):
	N, K = map(int, stdin.readline().strip().split())
	a,b = proper(N, K)
	print 'Case #%d: %d %d' %(caseNum + 1, b, a)

	

