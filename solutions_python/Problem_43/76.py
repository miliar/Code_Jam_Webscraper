import sys
import math

input = sys.stdin.readline().split()
T = int(input[0])

for t in xrange(T):
	input = sys.stdin.readline().strip()
	base = len(set(input))
	if base == 1: base = 2
	digitsleft = range(base)
	number = list(input)
	length = len(number)
	map = dict()
	pos = base ** (length - 1)
	value = 0
	#print "#", input, base, digitsleft, number, length, pos
	for i in range(length):
		#print "# value", value
		#print "# pos", pos
		#print "# i", i
		#print "# number[i]", number[i]
		#print "# digitsleft", digitsleft
		#if number[i] in map: print "##", map[number[i]]
		if i == 0:
			map[number[i]] = 1
			digitsleft.remove(1)
		elif number[i] not in map:
			map[number[i]] = min(digitsleft)
			digitsleft.remove(min(digitsleft))
		#print "#*#", map[number[i]] * pos
		value += map[number[i]] * pos
		pos /= base
		#print "###", value, pos, i, number[i], map[number[i]]
	print 'Case #%d: %d' % (t + 1, value)

