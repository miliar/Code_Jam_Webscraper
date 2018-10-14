#!/usr/bin/env python
import re

raw = int(raw_input())

def flipPancake(pancakes):
	return map(lambda x: "+" if x=="-" else "-", pancakes)

def rollOut(pancakes, batch):
	flipCount = 0
	length = len(pancakes)
	allHappyPattern = re.compile("[+]{%d}" % (length))

	if length < 2 or length > 1000:
		return "Impossible"

	if (allHappyPattern.match(pancakes)):
		return flipCount

	try:
		sets = pancakes
		while not allHappyPattern.match(sets):
			index = sets.index("-")
			outOfRange = index+int(batch)>=len(sets)
			batchCake = sets[-int(batch):] if outOfRange else sets[index:index+int(batch)]

			newSets = flipPancake(batchCake)
			splitSet = map(lambda x: x,sets)

			index = index if not outOfRange else len(sets)-int(batch)
			for i in range(int(batch)):
				splitSet[i+index] = newSets[i]

			sets = "".join(splitSet)
			
			flipCount += 1
			if sets == pancakes or flipCount > 1000:
				raise Exception("Impossible")

		return flipCount

	except Exception, e:
		return e
	

for i in range(raw):
	pancakes, flag = [test for test in raw_input().split(" ")]
	print "Case #{}: {}".format(i+1, rollOut(pancakes, flag))
	