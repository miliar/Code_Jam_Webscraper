def solve(N, R, O, Y, G, B, V):
	#if max(R, Y, B) > (N+1)/2:
	#	return 'IMPOSSIBLE'
	return assemble(R, Y, B)

def addOne(assembled, l1, c1, l2, c2):
	if c1 == 0 and c2 == 0:
		return 'IMPOSSIBLE'
	if c1 >= c2:
		return assembled + l1
	else:
		return assembled + l2

def addFirst(R, Y, B):
	if R == max(R, Y, B):
		return 'R'
	elif Y == max(R, Y, B):
		return 'Y'
	else:
		return 'B'

def addFinalLetters(assembled, counts):
	if max(counts['R'], counts['Y'], counts['B']) == 2:
		return 'IMPOSSIBLE'
	firstLetter = assembled[0]
	lastLetter = assembled[-1]
	if counts[firstLetter] > 0 and counts[lastLetter] > 0:
		if firstLetter == lastLetter:
			return 'IMPOSSIBLE'
		else:
			return assembled + firstLetter + lastLetter
	elif firstLetter != lastLetter and counts[firstLetter] > 0:
		assembled = assembled + firstLetter
		counts[firstLetter] -= 1
	remaining = []
	for c in ['R', 'Y', 'B']:
		if counts[c] > 0:
			remaining.append(c)
	if len(remaining) == 1:
		return addOne(assembled, firstLetter, 0, remaining[0], 1)
	assembled = addOne(assembled, remaining[0], 1, remaining[1], 1)
	return addOne(assembled, remaining[0], 0, remaining[1], 1)

def notMatchingLetterCounts(assmbled, R, Y, B):
	return assmbled.count('R') != R or assmbled.count('Y') != Y or assmbled.count('B') != B

def assemble(R, Y, B):
	counts = {
		'R': R,
		'Y': Y,
		'B': B
	}
	#print(counts)
	assembled = addFirst(R, Y, B)
	prevLetter = assembled[0]
	counts[prevLetter] -= 1
	while max(counts['R'], counts['Y'], counts['B']) > 0:
		if counts['R'] + counts['Y'] + counts['B'] == 2:
			assembled = addFinalLetters(assembled, counts)
			break
		if prevLetter == 'R':
			assembled = addOne(assembled, 'Y', counts['Y'], 'B', counts['B'])
		elif prevLetter == 'Y':
			assembled = addOne(assembled, 'B', counts['B'], 'R', counts['R'])
		elif prevLetter == 'B':
			assembled = addOne(assembled, 'R', counts['R'], 'Y', counts['Y'])
		if assembled == 'IMPOSSIBLE':
			break
		prevLetter = assembled[-1]
		counts[prevLetter] -= 1
	return assembled

if __name__ == '__main__':
	T = int(input().strip())
	for i in range(T):
		N, R, O, Y, G, B, V = map(int, input().strip().split(' '))
		sol = solve(N, R, O, Y, G, B, V)
		print('Case #{}: {}'.format(i+1, sol))