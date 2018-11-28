import re

fr = open("input.txt", 'r')
fw = open("output.txt", 'w')

lines = fr.readlines()

numTests = int(lines[0].strip())
curTest = 0
curLine = 1

def getLine():
	global curLine
	global lines
	curLine += 1
	return lines[curLine-1].rstrip()
	
def getMult():
	return getLine().strip().split()

def getMultInt():
	return map(int, getMult())
	
def getMultFloat():
	return map(float, getMult())

def fixDuplicates(a):
	lst = list(a)
	
	strt = len(lst)-1
	while strt > 0:
		while strt > 0 and lst[strt] == lst[strt-1]:
			lst.pop(strt-1)
			strt = strt - 1
		strt = strt - 1
			
	return ''.join(lst)
	
while curTest < numTests:	
	
	# ...
	N = int(getLine())
	L = []
	lS = None
	lS2 = None
	
	impossible = False
	
	for i in range(N):
		newL = getLine()
		stripped = fixDuplicates(newL)
		if lS is None:
			lS = stripped
			lS2 = ''.join(sorted(set(newL), key=newL.index))
		if lS != stripped:
			impossible = True
		L.append(newL)
	
	if impossible:
		s = "Fegla Won"
	else:
		total = 0
		s = ""
		d = 0
		for let in lS:
			totals = []
			for idx in range(len(L)):
				j = 0
				d = 0
				while j < len(L[idx]) and L[idx][j] == let:
					d = d + 1
					j = j + 1
				L[idx] = L[idx][j:]
				totals.append(d)
			totals = sorted(totals)
			total += totals[len(totals)-1] - totals[0]
		s = str(total)
		
	fw.write("Case #%d: %s\n" % (curTest+1, s))
	curTest += 1
					
fr.close()
fw.close()