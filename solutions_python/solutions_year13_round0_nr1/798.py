import sys
import pprint
numberOfCases = int(sys.stdin.readline())
for case in range(1, numberOfCases+1):
	numberOfVines = int(sys.stdin.readline())
	vines = [[int(number) for number in sys.stdin.next().split()] for x in xrange(numberOfVines)]
	pprint.pprint(vines)
	sys.stdout.write("Case #" + str(case) + ":\n")
