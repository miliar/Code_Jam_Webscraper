#!/usr/bin/env python

def getExtraFriends(args):
	Smax = args[0]
	strAudience = args[1]
	numStanding = 0
	extras = 0
	numExtras = 0
	debug = False

	for shylvl, numShy in enumerate(strAudience):
		if debug:
			print "Iteration: " + str(shylvl)
			print "Number of shy people: " + str(numShy)
			print "Number standing at the beginning: " + str(numStanding)

		if shylvl > numStanding:
			#print "Need extras"
			extras = shylvl - numStanding
		else:
			extras=0
		numStanding = numStanding + int(numShy) + extras
		numExtras+=extras

	return numExtras

def printAns(num, i):
	print "Case #" + str(i) + ": " + str(num)

def main():
	T = int(raw_input());
	for i in xrange(1, T+1):
		args = raw_input().split(' ')
		printAns(getExtraFriends(args), i)

main()
