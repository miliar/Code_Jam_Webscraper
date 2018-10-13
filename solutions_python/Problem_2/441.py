
import sys

filen=sys.argv[1]
f=open(filen,'r')

nC=f.readline().strip()
for i in xrange(int(nC)):
	tr = f.readline().strip()
	tr = int(tr)
	nA, nB = f.readline().strip().split(' ')

	listA=[]
	listB=[]
	for j in xrange(int(nA)):
		stTime, endTime = f.readline().strip().split(' ')
		nst, min = stTime.split(':')
		nst=int(nst)
		min=int(min)
		nst = nst*60 + min
		listA.append((nst, 1))
		
		nst, min = endTime.split(':')
		nst=int(nst)
		min=int(min)
		nst = nst*60 + min
		listB.append((nst+tr, -1))


	for j in xrange(int(nB)):
		stTime, endTime = f.readline().strip().split(' ')
		nst, min = stTime.split(':')
		nst=int(nst)
		min=int(min)
		nst = nst*60 + min
		listB.append((nst, 1))
		
		nst, min = endTime.split(':')
		nst=int(nst)
		min=int(min)
		nst = nst*60 + min
		listA.append((nst+tr, -1))

	listA.sort()
	listB.sort()
	#print listA
	#print listB
	
	newA=0
	stckA=0
	newB=0
	stckB =0
	for time, stckF in listA:
		stckA += stckF
		if stckA >0:
			newA+=1
			stckA=0

	for time, stckF in listB:
		stckB += stckF
		if stckB >0:
			newB+=1
			stckB=0
	print "Case #"+str(i+1)+": "+str(newA)+" "+str(newB)
		
		
