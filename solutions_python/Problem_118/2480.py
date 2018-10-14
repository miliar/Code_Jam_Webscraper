import math

"""For Small Input File"""
inFile = open("C-small-attempt0.in", "r")
outFile = open("C-small-attempt0.out", "w")

"""For Large Input File
inFile = open("", "r")
outFile = open("", "w")"""

"""For Second Large Input File
inFile = open("", "r")
outFile = open("", "w")"""

T = int(inFile.readline())
total = 0
for i in range(T):
	items = map(int, inFile.readline().split())
	for j in range(items[0], items[1]+1):
		if str(j) == str(j)[::-1]:
			if int(math.sqrt(j)) == math.sqrt(j):
				if str(int(math.sqrt(j))) == str(int(math.sqrt(j)))[::-1]:
					total += 1
	outFile.write("Case #%d: %d" % (i + 1, total) + "\n")
	total = 0

inFile.close()
outFile.close()