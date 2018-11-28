

import sys
sys.setrecursionlimit(10000)


file = open('A-large.in','r')
testCases = int(file.readline())


def flip(idx, round, pancackes, flipper):
	down = pancackes.find('-');

	if down < 0:
		print 'Case #' + str(idx) + ':', round
	elif (down+flipper) > len(pancackes):
		print 'Case #' + str(idx) + ': IMPOSSIBLE'
	else:
		# flip!
		l = list(pancackes)
		for flipIdx in range(0,flipper):
			if l[down+flipIdx] == '-':
				l[down+flipIdx] = '+'
			else:
				l[down+flipIdx] = '-'

		pancackes = ''.join(l)
		#print pancackes
		flip(idx, round+1, pancackes[down+1:], flipper)



for i in range(0,testCases):
	line = file.readline().strip()
	split = line.split( )
	pancackes = split[0]
	flipper = int(split[1])

	flip(i+1, 0, pancackes, flipper)


