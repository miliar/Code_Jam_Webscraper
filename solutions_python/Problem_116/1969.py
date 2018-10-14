#!/usr/bin/python
import sys

resP = {"." : "Game has not completed", "X" : "X won", "O" : "O won", "Z" : "Draw"}

def checkl(arr):
	if '.' in arr:
		return "."

	if ('X' in arr ) and ('O' in arr ):
		return "Z"

	if 'X' in arr :
		return 'X'
	
	if 'O' in arr:
		return 'O'


def doarr(allin):
	#print "DOarr:", allin
	### check line
	alls = []
	for i in range(0,4):
		alls.append(allin[i][:])
	for i in range(0,4):
		ta = []
		for j in range(0,4):
			ta.append(allin[j][i])
		alls.append(ta)

	arr = [allin[0][0],allin[1][1], allin[2][2], allin[3][3]]
	alls.append(arr)
	arr = [allin[3][0],allin[2][1], allin[1][2], allin[0][3]]
	alls.append(arr)
	#print "ALL to check", alls

	res = []
	for line in alls:
		rest = checkl(line)
		#print line, " result " ,rest
		if rest in ['X', 'O'] :
			return rest
		res.append(rest)

	if '.' in res:
		return '.'

	return 'Z'

def treatpart(part, j):
	#print ""
	#print "=============="
	if len(part)!=4:
		return 
	#print part
	allin = []
	for line in part:
		arr = []
		if len(line) != 4:
			return 
		for i in range(0, 4):
			arr.append(line[i])

		allin.append(arr)
	res = doarr(allin)
	print "Case #%d: %s"%(j, resP[res])

def testmain():
	if(len(sys.argv)<2):
		return

	fname = sys.argv[1]
	f = open(fname)
	line=f.readline()
	Ts = int(line.strip())
	
	#print Ts
	j=0
	part = []
	while True:
		if(j>Ts):
			return
		line=f.readline()
		#print "read " ,line
		if(len(line)<=0):
			#print "line less"
			break
		
		line = line.strip()
		if(len(line) == 0):
			treatpart(part, j+1)
			
			part = []
			j+=1
		else:
			part.append(line)
		#print "Case #%d: %d"%(j, res)
	treatpart(part, j+1)
	
if __name__ == "__main__":
	testmain()
