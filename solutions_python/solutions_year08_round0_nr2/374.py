#!/usr/bin/env python

import sys

def time2sec(t):
    hour, minute = map(int, t.split(":"))
    return hour*60+minute

class TrainDepot:
    def __init__(self):
	self.provided=0
	self.available=[]
    def arrivesTrain(self, arrivaltime):
	self.available.append(arrivaltime+turnaroundtime)
	self.available.sort()
    def departsTrain(self, departuretime):
	if len(self.available)>0 and self.available[0]<=departuretime:
	    del self.available[0]
	else:
	    self.provided+=1
    def trainsProvided(self):
	return self.provided

filename=sys.argv[1]
inputfile=file(filename, 'r')
numcases=int(inputfile.readline().strip())
for case in range(1,numcases+1):
    turnaroundtime=int(inputfile.readline().strip())
    NA, NB = map(int, inputfile.readline().strip().split(" "))
    trips=[]
    for i in range(NA):
	dep, arr = map(time2sec, inputfile.readline().strip().split(" "))
	trips.append(('A',dep,arr))
    for i in range(NB):
	dep, arr = map(time2sec, inputfile.readline().strip().split(" "))
	trips.append(('B',dep,arr))
    trips.sort(lambda x,y: cmp(x[1], y[1]))
    depotA = TrainDepot()
    depotB = TrainDepot()
    for (start_depot, dep, arr) in trips:
	if start_depot=='A':
	    depotA.departsTrain(dep)
	    depotB.arrivesTrain(arr)
	else:
	    depotB.departsTrain(dep)
	    depotA.arrivesTrain(arr)
    print "Case #%d: %d %d" % (case, depotA.trainsProvided(), depotB.trainsProvided())
