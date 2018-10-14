import sys


def calculateNumMoves(parts):
	moves = 0
	new = zip(*parts)
	for part in new:
		avg = sum([len(x) for x in part])/len(part)
		print 'average shoudl be: ' + part[0][0]*avg
		for item in part:
			moves += abs(len(item)-avg)
	return moves
def confirmIdentities(identities):
	new = zip(*identities)
	if len(new[0]) != len(identities):
		return False
	for identity in new:
		ch = identity[0]
		for i in range(1, len(identity)):
			if identity[i] != ch:
				return False
	return True

def compareStrings(strings):
	for i in range(0, len(strings)):
		array = list(strings[i])
		for j in range(i, len(strings)):
			for ch in strings[j]:
				if ch not in array:
					return False
	return True

def splitToParts(string):
	array = [string[0]]
	for ch in string[1:]:
		if ch == array[-1][-1]:
			array[-1] = array[-1] + ch
		else:
			array += [ch]
	return array

def splitToIdentities(string):
	array = [string[0]]
	for ch in string[1:]:
		if ch != array[-1][-1]:
			array += [ch]
	return array

infile = sys.argv[1]
outfile = sys.argv[2]

inf = open(infile)
outf = open(outfile, 'w')
numTestCases = int(inf.readline())

for testcase in range(1, numTestCases+1):
	N = int(inf.readline())
	strings = []
	for s in range(0, N):
		strings += [inf.readline()]
	#first check
	firstcheck = compareStrings(strings)
	if firstcheck == False:
		outf.write('Case #'+str(testcase)+': Fegla Won\n')
	else:
		identities = [splitToIdentities(string) for string in strings]
		secondcheck = confirmIdentities(identities)
		if secondcheck == False:
			outf.write('Case #'+str(testcase)+': Fegla Won\n')
		else:
			parts = [splitToParts(string) for string in strings]
			numMoves = calculateNumMoves(parts)
			outf.write('Case #'+str(testcase)+': '+str(numMoves)+'\n')