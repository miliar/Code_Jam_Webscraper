import sys
import math
import numpy as np

sys.setrecursionlimit(10000)


file = open('C-small-1-attempt1.in','r')
testCases = int(file.readline())


def splitStalls(stalls, people, list, result):

	if people <= 0:
		return result

	if stalls <= 1:
		return (0,0)

	elif stalls == 2:
		list = [1] + list
		return splitStalls(list.pop(), people-1, list, (1,0))

	else:

		# even number
		if stalls % 2 == 0:
			div = int(math.floor(stalls / 2)) 
			list = [div-1, div] + list
			list = np.sort(list).tolist()
			result = (div, div-1)
		else:
			div = int(math.floor(stalls / 2))
			list = [div, div] + list
			result = (div, div)

		return splitStalls(list.pop(), people-1, list, result)


for i in range(0,testCases):
	line = file.readline().strip().split( )

	stalls = float(line[0])
	people = int(line[1])

	res = splitStalls(stalls, people, [], (0,0))
	print 'Case #' + str(i+1) + ': ' + str(res[0]) + ' ' +  str(res[1])

	

