#!/usr/bin/env python3
import sys

def war(naomisblocks, kensblocks):
	naomipoints = 0
	for chosennaomi in naomisblocks:
		if kensblocks[-1] < chosennaomi:
			chosenken = kensblocks[0]
			kensblocks.pop(0)
		else:
			for block in kensblocks:
				if block > chosennaomi:
					chosenken = block
					kensblocks.remove(chosenken)
					break
		if chosennaomi > chosenken:
			naomipoints += 1
	return naomipoints

def deceitfulwar(naomisblocks, kensblocks):
	naomipoints = 0
	add = 0
	while True:
		if naomisblocks[-1] < kensblocks[0]:
			chosennaomi = naomisblocks.pop()
			toldnaomi = chosennaomi
		else:
			for block in naomisblocks:
				if block > kensblocks[0]:
					chosennaomi = block
					naomisblocks.remove(block)
					add += 0.0000001
					toldnaomi = kensblocks[-1] + add
					break
		if kensblocks[-1] < toldnaomi:
			chosenken = kensblocks[0]
			kensblocks.pop(0)
		else:
			for block in kensblocks:
				if block > toldnaomi:
					chosenken = block
					kensblocks.remove(chosenken)
					break
		if chosennaomi > chosenken:
			naomipoints += 1
		if not naomisblocks:
			break
	return naomipoints

argc = len(sys.argv)
filename = sys.argv[1]
if argc > 2:
	casenumbers = list(map(int, sys.argv[2:]))
file = open(filename)
T = int(file.readline().rstrip())
for case in range(1,T+1):
	N = int(file.readline().rstrip())
	naomisblocks = list(map(float, (file.readline().rstrip().split())))
	kensblocks = list(map(float, (file.readline().rstrip().split())))
	if argc > 2 and not(case in casenumbers):
		continue
	naomisblocks.sort()
	kensblocks.sort()
	warscore = war(naomisblocks[:], kensblocks[:])
	deceitfulwarscore = deceitfulwar(naomisblocks[:], kensblocks[:])
	print ("Case #", case, ": ", sep="", end="")
	print(deceitfulwarscore, warscore)
