#!/usr/bin/python
import sys


def readTestCases(input_file):
	i = 0
	f = open(input_file)
	numTestCases = int(f.readline())
	while i < numTestCases:
		sMax, audienceShyness = f.readline().split()
		print "Case #%d: %d" %(i + 1, findNumFriend(sMax, audienceShyness))
		i += 1


def findNumFriend(sMax, audienceShyness):
	numFriends = 0
	numStanding = 0
	i = 0
	audList = list(audienceShyness)
	for i in range(int(sMax) + 1):
		# print "numStanding = " + str(numStanding)
		# print "i = " + str(i)
		if numStanding < i and i < sMax and int(audList[i]) != 0:
			numFriends += i - numStanding
			# print "numFriends = " + str(numFriends)
			numStanding += numFriends
		if i < len(audList):
				numStanding += int(audList[i])
	return numFriends

if __name__ == '__main__':
	readTestCases(sys.argv[1])
