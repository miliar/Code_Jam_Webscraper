import pdb
import sys

def task(inFile):
	line = next(inFile)
	numbers = [int(n) for n in list(line) if n != ' ' and n != '\n']
	maxShynes = numbers.pop(0)
	nFriends = 0
	nClapping = 0
	for x in range(maxShynes + 1):
		p = numbers[x]
		if p == 0: 
			continue
		if nClapping >= x:
			nClapping = nClapping + p
		else:
			nFriends = nFriends + x - nClapping
			nClapping = x + p
	return nFriends

output = open('output.txt',  mode='w', encoding='utf-8')

with open(sys.argv[1], encoding='utf-8') as inFile:
	T = int(next(inFile))

	for t in range(0,T):
		output.write('Case #{0}: {1}\n'.format(t+1, task(inFile)))