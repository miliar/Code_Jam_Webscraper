text = open("B-small-attempt2.in")
numCases = int(text.readline())

#use numpy
import math

for i in xrange(numCases):	
	numDiners = int(text.readline())
	cakeDist = map(int,text.readline().split())
	maxSplits = max(cakeDist)
	minTime = max(cakeDist)	
	#print cakeDist
	#print "Max Splits:",maxSplits

	for j in xrange(maxSplits):
		jSplitDist = list(cakeDist)
		minutes1 = 0
		#print "Iteration:", j
		while sum(jSplitDist) > 0:
			if minutes1 >= minTime:
				#make it faster
				break
			elif minutes1 < j:
				index = jSplitDist.index(max(jSplitDist))
				cakes = jSplitDist[index]
				jSplitDist[index] =  int(math.floor(cakes/2.0))
				jSplitDist.append(int(math.ceil(cakes/2.0)))
				minutes1 += 1
			else:
				jSplitDist = map(lambda x: x - 1, jSplitDist)
				jSplitDist = filter(lambda a: a != 0, jSplitDist)
				minutes1 += 1
		
		jSplitDist = list(cakeDist)
		minutes2 = 0
		#print "Iteration:", j
		while sum(jSplitDist) > 0:
			if minutes2 >= minTime:
				#make it faster
				break
			elif minutes2 < j:
				index = jSplitDist.index(max(jSplitDist))
				cakes = jSplitDist[index]
				if(cakes % 2 == 0):
					jSplitDist[index] =  int(math.floor(cakes/2.0))
					jSplitDist.append(int(math.ceil(cakes/2.0)))
				else:
					jSplitDist[index] =  int(math.floor(cakes/3.0))
					jSplitDist.append(int(math.ceil(2*cakes/3.0)))
				minutes2 += 1
			else:
				jSplitDist = map(lambda x: x - 1, jSplitDist)
				jSplitDist = filter(lambda a: a != 0, jSplitDist)
				minutes2 += 1



			#print jSplitDist
			#print minutes
			
		if(min(minutes1,minutes2) < minTime):
			minTime = min(minutes1,minutes2)
		
	print "Case #" + str(i+1) + ": " + str(minTime)
