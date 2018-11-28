#! /usr/bin/python
# _*_ coding: utf-8 _*_

import sys
import struct

def checkUsage():
	rc = True
	if (len(sys.argv) != 2):
		print "Usage:python %s InputFileName" % sys.argv[0]
		rc = False
	return rc
	
def rFileOpen(fileName):
	return open(fileName,'r')

def BlockRead(fObj):

	recordFormat = '4c'
	rDatas = []
	i = 0

	while True:
		rData = fObj.readline()
		if not rData:
			break

		if rData == '\n':
			break

		rDatas.append(struct.unpack(recordFormat,rData.rstrip('\n')))

	return rDatas

def checkGame(datas,case):

	rCountX=3
	rCountY=0
	rCountXX=0
	rCountOO=0
	lCountX=0
	lCountY=0
	lCountXX=0
	lCountOO=0

	xCountX = 0
	xCountY = [0,0,0,0]
	oCountX = 0
	oCountY = [0,0,0,0]
	dCount = 0

	for y in range(4):
		for x in range(4):
			if datas[y][x] == 'X':
				xCountY[x]+=1 
				xCountX+=1 
				if (rCountX == x and rCountY == y):
					rCountXX+=1 
				if (lCountX == x and lCountY == y):
					lCountXX+=1 
			if datas[y][x] == 'O':
				oCountX+=1 
				oCountY[x]+=1 
				if (rCountX == x and rCountY == y):
					rCountOO+=1 
				if (lCountX == x and lCountY == y):
					lCountOO+=1 
			if datas[y][x] == 'T':
				xCountY[x]+=1 
				oCountY[x]+=1 
				xCountX+=1 
				oCountX+=1 
				if (rCountX == x and rCountY == y):
					rCountXX+=1 
					rCountOO+=1 
				if (lCountX == x and lCountY == y):
					lCountXX+=1 
					lCountOO+=1 
			if datas[y][x] == '.':
				dCount+=1 

		if xCountX == 4:
			print "Case #%d: X won" % case
			break

		if oCountX == 4:
			print "Case #%d: O won" % case
			break
		xCountX = 0
		oCountX = 0
		rCountX-=1
		rCountY+=1
		lCountX+=1
		lCountY+=1

	if xCountX != 4 :
		if oCountX != 4 :
			if xCountY[0] == 4 or xCountY[1] == 4 or xCountY[2] == 4 or xCountY[3] == 4:
				print "Case #%d: X won" % case
			elif oCountY[0] == 4 or oCountY[1] == 4 or oCountY[2] == 4 or oCountY[3] == 4:
				print "Case #%d: O won" % case
			elif rCountXX == 4 :
				print "Case #%d: X won" % case
			elif lCountXX == 4 :
				print "Case #%d: X won" % case
			elif rCountOO == 4 :
				print "Case #%d: O won" % case
			elif lCountOO == 4 :
				print "Case #%d: O won" % case
			elif dCount == 0 :
				print "Case #%d: Draw" % case
			else :
				print "Case #%d: Game has not completed" % case

if __name__ == "__main__":
	rc = checkUsage()
	if (rc != True):
		quit();
	fObj = rFileOpen(sys.argv[1])

	roopNumberString = fObj.readline().rstrip('\n')

	roopNumber = int(roopNumberString)	
	for i in range(roopNumber):	
		rDatas = BlockRead(fObj)
#		print "Case#%(case)d " % {"case":i+1}
		checkGame(rDatas,i+1)

	fObj.close


