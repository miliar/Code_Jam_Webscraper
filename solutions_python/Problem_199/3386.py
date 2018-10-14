from collections import deque

file = open("pancake.in", "r")
numCases = int(file.readline())

# 01010010 3
# 10110010
# 10110101

def xor(inp, i, K):
	newString = ''
	for ii in range(i, i + K):
		c = inp[ii]
		if c == '+':
			newString += '-'
		else:
			newString += '+'

	return inp[:i] + newString + inp[i + K:]

def actions(inp, N, K):
	for i in range(N - K + 1):
		yield xor(inp, i, K)


def run(inp, K):
	inpLen = len(inp)
	#print('run:', inp)

	target = inp.replace('-', '+')

	#print('target', target)

	visited = {}
	visited[inp] = 0
	queue = deque()
	queue.append(inp)

	while len(queue) > 0:
		item = queue.popleft()
		currStep = visited[item]

		if item == target:
			#jupii
			return currStep

		for action in actions(item, inpLen, K):
			#print(action)

			if not action in visited:
				visited[action] = currStep + 1
				queue.append(action)



for caseId in range(numCases):
	line = file.readline()
	[inp, K] = line[:-1].split(' ')
	steps = run(inp, int(K))
	if steps == None:
		print('Case #%d: IMPOSSIBLE' % (caseId + 1))
	else:
		print('Case #%d: %d' % (caseId + 1, steps))

