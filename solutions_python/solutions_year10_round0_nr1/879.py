#Code Jam 2010 - Qualifiers - A
#Daniel Bjorge
import os,sys

def isOn(n, k):
	tn = 2 ** n
	return k % tn == tn - 1

with open(sys.argv[1]) as infile:
	with open(sys.argv[1]+".out","w") as outfile:
		lineNum = -1
		for line in infile:
			lineNum += 1
			if lineNum == 0:
				continue
			parts = line.strip().split(" ")
			n,k = int(parts[0]), int(parts[1])
			on = isOn(n,k)
			if on:
				resStr = "ON"
			else:
				resStr = "OFF"
			outfile.write("Case #%d: %s\n" % (lineNum, resStr))