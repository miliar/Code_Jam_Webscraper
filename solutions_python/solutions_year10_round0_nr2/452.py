#!/usr/bin/python
import sys

def pgcd(a, b):
	if b == 0:
		return pgcd(b, a)
	if a % b == 0:
		return b
	return pgcd(b, a % b)

testIn = open(sys.argv[1], "r")
testOut = open(sys.argv[2], "w")

nbTests = int(testIn.readline())
nbTest = 1

while nbTest <= nbTests:
	line = testIn.readline().split(" ")
	nbEvents = int(line[0])
	events = line[1:]
	for i in range(nbEvents):
		events[i] = int(events[i])

	events.sort()

	mini = events[0]
	gcd = events[1]-mini
	events = events[2:]

	while events:
		gcd = pgcd(gcd, events[-1]-mini)
		events = events[:-1]

	next = mini%gcd
	if not next == 0:
		next = gcd-next

	outLine = "Case #"+str(nbTest)+": "+str(next)
	print outLine
	testOut.write(outLine+"\n")

	nbTest += 1
