

import sys


f = open("A-large.in")

f2 = open("outp", "w")
testcases = int(f.readline())

#for i in xrange(testcases):
case = 1
for line in f:
	highest, levels = line.split()
	highest = int(highest)	
	tot = int(levels[0])
	needed = 0
	for j in xrange(1, highest + 1):
		added_friends = max(0, j - tot)
		needed += added_friends
		tot += int(levels[j]) + added_friends
	f2.write("Case #" + str(case) + ": " + str(needed) + "\n")
	case += 1
