
import sys
import math

def readInput(filePath):
	data = { 'nCase' : 0, 'cases' : [] }
	f = open(filePath, 'r')
	data['nCase'] = int(f.readline())
	for i in range(0, data['nCase']):
		factors = map(lambda x: float(x), f.readline().split(' '))
		data['cases'].append(factors)

	return data

def getAnswer(case):
	factorC = case[0]
	factorF = case[1]
	factorX = case[2]
	baseRate = 2

	answer = factorX / baseRate

	# t = Sum(0, n-1) ( C/(2+nF) ) + X/(2+nF), n>=1
	n = 1
	secFarm = 0
	while (True):
		secFarm = secFarm + factorC / (baseRate + (n - 1) * factorF)

		totalSec = secFarm + factorX / (baseRate + n * factorF)
		
		if totalSec < answer:
			answer = totalSec
		else:
			break;
		n = n + 1

	return answer


def main(argv):
	if len(argv) != 3:
		print 'Usage: main <input_file> <output_file>'
		return

	data = readInput(argv[1])
	output = open(argv[2], 'w')
	for idx, val in enumerate(data['cases']):
		answer = getAnswer(val)
		output.write('Case #%d: %.7f\n' % (idx + 1, answer))

main(sys.argv)

