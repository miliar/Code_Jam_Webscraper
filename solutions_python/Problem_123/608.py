#!C:\Python33\python
import sys
import fileinput

sys.path.append(r'D:\Data\Programming\Code Jam\Libraries')
from CodeJamLib import *

def main ():
	lines = fileinput.input()
	cases = int(lines.readline())
	for case in range(1, cases + 1):
		armin, moteCount = readInts(lines.readline())
		motes = readInts (lines.readline())
		print ("Case #{0}: {1}".format(case, operations(armin, motes)))

def operations (armin, motes):
	motes.sort()
	currentSize = armin
	biggerMotes = []
	operations = 0
	
	for mote in motes:
		if currentSize > mote:
			currentSize += mote
			
		else:
			biggerMotes.append(mote)
	
	if len(biggerMotes) == 0:
		return 0
	
	while True:
		testSize = currentSize
		current = 1
		while True:
			testSize += testSize - 1
			biggerMotes.sort()
			testSize2 = testSize
			eatable = 0
			for mote in biggerMotes:
				if testSize2 > mote:
					testSize2 += mote
					eatable += 1
					
				else:
					break
				
			if eatable >= current:
				operations += current
				currentSize = testSize2
				biggerMotes = [mote for mote in biggerMotes if currentSize <= mote]
				break
				
			if current >= len(biggerMotes):
				return operations + len(biggerMotes)
			
			current += 1
			
	return operations
	
main()