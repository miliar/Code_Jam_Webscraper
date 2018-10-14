'''
Created on 2014/04/12

@author: Chocolatle
'''

import sys

def main():
	numberOfTestCase = int(sys.stdin.readline().lstrip())

	for testCase in xrange(numberOfTestCase):
		previousRowNumber = int(sys.stdin.readline().lstrip())
		previousMatrix = []
		for n in xrange(4):
			previousMatrix.append( [int(i) for i in sys.stdin.readline().lstrip().split()] )
		previousRow = previousMatrix[previousRowNumber - 1]

		currentRowNumber = int(sys.stdin.readline().lstrip())
		currentMatrix = []
		for n in xrange(4):
			currentMatrix.append( [int(i) for i in sys.stdin.readline().lstrip().split()] )
		currentRow = currentMatrix[currentRowNumber - 1]

		res = 0
		for target in currentRow:
			if previousRow.count(target) > 0:
				ans = target
			res += previousRow.count(target)
		if res == 1:
			print "Case #%d: %d"  % (testCase + 1, ans)
		elif res > 1:
			print "Case #%d: Bad magician!" % (testCase + 1)
		else:
			print "Case #%d: Volunteer cheated!" % (testCase + 1)



if __name__ == '__main__':
	main()