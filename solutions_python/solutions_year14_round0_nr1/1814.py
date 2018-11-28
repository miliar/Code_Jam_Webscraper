#!/usr/bin/env python

tc = int(input())

bad = "Bad magician!"
cheater = "Volunteer cheated!"

def getLine(pos):
	lines = [input() for _ in range(4)]
	return lines[pos]

def line2Arr(line):
	c = line.split()
	ret = []
	for n in c:
		ret += [int(n)]
	return ret

for t in range(tc):
    pos = int(input())
    firstLine = line2Arr(getLine(pos-1))
    pos = int(input())
    secondLine = line2Arr(getLine(pos-1))
    

    #print("1st line", firstLine)
    #print("2nd line", secondLine)

    #intersect = [filter(lambda x: x in firstLine, sublist) for sublist in secondLine]
    intersect = set(firstLine).intersection(secondLine)
    
    if len(intersect) == 0:
        result = cheater
    elif len(intersect) == 1:
        result = str(list(intersect)[0])
    else:
        result = bad

    print("Case #"+str(t+1)+": " + result)