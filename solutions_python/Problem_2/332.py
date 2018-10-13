#! /usr/bin/python

def stringToMinutes(timestring):
        (hr,min) = timestring.split(":")
        minutes = int(hr)*60 + int(min)
        return minutes

inpfile = open('in3', 'r')

inpCount = int (inpfile.readline())
ind = 0
case = 0
while ind < inpCount:
	turnAroundTime = int(inpfile.readline())

	startCnt = inpfile.readline()
	(aCnt,bCnt) = startCnt.split(" ")
	(aCnt,bCnt) = (int(aCnt),int(bCnt))
	#print aCnt
	#print bCnt
	tempCnt = 0
	f = []
	while tempCnt < aCnt + bCnt :
		f.append(inpfile.readline())
		tempCnt = tempCnt + 1	
	#print f

	(aStart,aEnd) = ([],[])
	(bStart,bEnd) = ([],[])
	count = 0

	for i in f:
		if count < aCnt:
			(aStart1,aEnd1) = i.strip("\n").split(" ")
			aStart.append(aStart1),aEnd.append(aEnd1)
		else :
			(bStart1,bEnd1) = i.strip("\n").split(" ")
			bStart.append(bStart1),bEnd.append(bEnd1)
		count = count + 1
	#print aStart,aEnd,bStart,bEnd

	(aStartMins,bStartMins,aEndMins,bEndMins)=([],[],[],[])
	for i in aStart:
		aStartMins.append(stringToMinutes(i))
	for j in aEnd:
		aEndMins.append(stringToMinutes(j))
	for k in bStart:
		bStartMins.append(stringToMinutes(k))
	for l in bEnd:
		bEndMins.append(stringToMinutes(l))

	(a1,a2,b1,b2) = (sorted(aStartMins),sorted(aEndMins),sorted(bStartMins),sorted(bEndMins))

	while a1 and b2:
		if a1[0] >= b2[0] + turnAroundTime:
			aCnt = aCnt - 1
			a1.remove(a1[0])
			b2.remove(b2[0])
		else:
			a1.remove(a1[0])

	while b1 and a2:
        	if b1[0] >= a2[0] + turnAroundTime:
                	bCnt = bCnt - 1
	                b1.remove(b1[0])
        	        a2.remove(a2[0])
	        else:
        	        b1.remove(b1[0])
	
	case = ind + 1
	print "Case #%d: %d %d" % (case,aCnt,bCnt)
	ind = ind + 1	
