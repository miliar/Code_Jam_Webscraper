#!/usr/local/bin/python
#set-encoding=UTF-8

import fileinput

def Time2Integer(atime):
	retval = 0
	pieces = atime.split(':')
	hh = int(pieces[0])
	mm = int(pieces[1])
	retval = hh*60+mm
	return retval

def GetNumberOfTrains(depart, arrival, turnaroundtime):
	retval = 0
	indexA = 0

	depart.sort()
	arrival.sort() 

	if len(arrival) == 0:
		retval = len(depart)
	else:
		for train in depart:
			if indexA < len(arrival) and train >= (arrival[indexA] + turnaroundtime):
				indexA += 1
			else:
				retval += 1 

	return retval


problems = 0
nproblem = 0
turntime = -1
tripinfo = -1
NA       = -1
NB       = -1
OutA     = []
InB      = []
OutB     = []
InA      = []
NTrainA  = 0
NTrainB  = 0

if __name__ == "__main__":

	for line in fileinput.input():

		if fileinput.isfirstline():
			#Reading number of cases
			problems = int(line.strip('\n'))

		if 1 < fileinput.filelineno() and nproblem < problems:
			if turntime < 0:
				turntime = int(line.strip('\n'))
			elif tripinfo < 0:
				triminfo = line.strip('\n')
				pieces = triminfo.split(' ')
				NA = int(pieces[0])
				NB = int(pieces[1])
				tripinfo = 0
			elif NA > 0:
				schedule = line.strip('\n')
				pieces   = schedule.split(' ')
				OutA.append(Time2Integer(pieces[0]))
				InB.append(Time2Integer(pieces[1]))
				NA -= 1
				if NA == 0 and NB == 0:
					NTrainA = GetNumberOfTrains(OutA, InA, turntime)
					NTrainB = GetNumberOfTrains(OutB, InB, turntime)
					nproblem += 1
					print "Case #%d: %d %d" % (nproblem, NTrainA, NTrainB)
					turntime = -1
					tripinfo = -1
					NA       = -1
					NB       = -1
					del OutA[:]
					del OutB[:]
					del  InA[:]
					del  InB[:]
			elif NB > 0:
				schedule = line.strip('\n')
				pieces   = schedule.split(' ')
				OutB.append(Time2Integer(pieces[0]))
				InA.append(Time2Integer(pieces[1]))
				NB -= 1
				if NB == 0:
					NTrainA = GetNumberOfTrains(OutA, InA, turntime)
					NTrainB = GetNumberOfTrains(OutB, InB, turntime)
					nproblem += 1
					print "Case #%d: %d %d" % (nproblem, NTrainA, NTrainB)
					turntime = -1
					tripinfo = -1
					NA       = -1
					NB       = -1
					del OutA[:]
					del OutB[:]
					del  InA[:]
					del  InB[:]
