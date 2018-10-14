
import sys
import math

def readInput(filePath):
	data = { 'nCase' : 0, 'cases' : [] }
	f = open(filePath, 'r')
	data['nCase'] = int(f.readline())
	for i in range(0, data['nCase']):
		n = int(f.readline())
		p1 = map(lambda x: float(x), f.readline().split(' '))
		p2 = map(lambda x: float(x), f.readline().split(' '))
		p1 = p1[0:n]
		p2 = p2[0:n]
		p1.sort()
		p2.sort()
		data['cases'].append({
			'n' : n,
			'p1' : p1,
			'p2' : p2
		})

	return data

def getDeceitfulAnswer(case):
	n = case['n']
	p1 = case['p1']
	p2 = case['p2']

	winCount = 0
	for i in range(0, n):
		if (p1[-1] < p2[-1]):
			p1 = p1[1:]
			p2 = p2[:-1]
		elif (p1[-1] > p2[-1]):
			p1 = p1[:-1]
			p2 = p2[:-1]
			winCount = winCount + 1

	return winCount

def getWarAnswer(case):
	n = case['n']
	p1 = case['p1']
	p2 = case['p2']

	winCount = 0
	for i in range(0, n):
		p1M = p1[0]
		p2M = p1[0]
		if (p1M < p2M):
			del p1[0]
			del p2[0]
		else:
			#find greater than p1M
			found = False
			for j in range(n - i):
				if p1M < p2[j]:
					del p2[j]
					del p1[0]
					found = True
					break;

			if found == False:
				del p1[0]
				del p2[0]
				winCount = winCount + 1

	return winCount

def main(argv):
	if len(argv) != 3:
		print 'Usage: main <input_file> <output_file>'
		return

	data = readInput(argv[1])
	output = open(argv[2], 'w')
	for idx, val in enumerate(data['cases']):
		answerDeceitful = getDeceitfulAnswer(val)
		answerWar = getWarAnswer(val)
		output.write('Case #%d: %d %d\n' % (idx + 1, answerDeceitful, answerWar))

main(sys.argv)

