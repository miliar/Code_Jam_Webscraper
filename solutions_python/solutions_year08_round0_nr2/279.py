import sys
import math

def readCJIn(filename):
	"""Reads the file.
	
	This function reads Google Code Jam input files and returns the number of inputs and a list containing the inputs"""
	file = open(filename)
	inputs = []
	for line in file:
		inputs.append(line.strip())
	file.close()
	return int(inputs[0]),inputs[1:len(inputs)]

def feq(a,b):
	"""Returns true if the difference between a and b are less than 1e-6"""
	if math.fabs(a-b)<0.000001:
		return True
	return False

inmag, inputs = readCJIn(sys.argv[1])

def convtime(timestr):
	time = timestr.split(":")
	return ((int(time[0])*60)+int(time[1]))

for i in range(0,inmag):
	ccase = i+1
	ttime = int(inputs[0])
	inputs = inputs[1:]
	nanb = [int(x) for x in inputs[0].split(" ")]
	na, nb = (nanb[0],nanb[1])
	inputs = inputs[1:]
	asch = inputs[:na]
	inputs = inputs[na:]
	bsch = inputs[:nb]
	inputs = inputs[nb:]

	ad = []
	ba = []
	for sch in asch:
		schsep = sch.split(" ")
		ad.append(convtime(schsep[0]))
		ba.append(convtime(schsep[1]))
	bd = []
	aa = []
	for sch in bsch:
		schsep = sch.split(" ")
		bd.append(convtime(schsep[0]))
		aa.append(convtime(schsep[1]))
	
	ad.sort()
	ba.sort()
	bd.sort()
	aa.sort()

	aneed = 0
	index = 0
	aamag = len(aa)
	for d in ad:
		if index>=aamag or aa[index]+ttime>d:
			aneed+=1
		else:
			index+=1
	bneed = 0
	index = 0
	bamag = len(ba)
	for d in bd:
		if index>=bamag or ba[index]+ttime>d:
			bneed+=1
		else:
			index+=1

	print "Case #%d: %d %d" % (ccase,aneed,bneed)
