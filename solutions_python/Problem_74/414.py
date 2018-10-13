#!/usr/bin/env python

def solveCase(data):
	curRob = ""
	myPos = 1; prevPos = 1
	dt = 0
	elapsed = 0
	while len(data) > 0:
		rob = data.pop(0); button = int(data.pop(0))
		if curRob == "": curRob = rob
		needed = abs(button - myPos) + 1
		if rob != curRob:
			curRob = rob
			myPos, prevPos = prevPos, myPos
			needed = abs(button - myPos)
			if elapsed > needed:
				needed = 0
			else:
				needed = needed - elapsed
			needed += 1
			elapsed = 0
		dt += needed
		elapsed += needed
		myPos = button
	return dt

def main():
	T = input()

	for i in range(T):
		data = raw_input()
		data = data.split()
		N = data.pop(0)
		print "Case #%d: %d" % (i+1, solveCase(data))

	return
main()

