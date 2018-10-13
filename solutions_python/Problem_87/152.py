import sys

def sortP(P):
	for i in xrange(len(P)-1):
		for j in xrange(len(P)-i-1):
			if P[j][1]>P[j+1][1]:
				for k in xrange(2):
					P[j][k],P[j+1][k]=P[j+1][k],P[j][k]

T=int(raw_input())
for repeat in xrange(T):
	confLine=raw_input().split()
	X,S,R,t,N=int(confLine[0]),int(confLine[1]),int(confLine[2]),int(confLine[3]),int(confLine[4])
	t*=1.
	W=[]
	for i in xrange(N):
		walkLine=raw_input().split()
		W+=[[int(walkLine[0]),int(walkLine[1]),int(walkLine[2])]]
	sumW=0
	for i in xrange(N):
		sumW+=W[i][1]-W[i][0]
	P=[]
	if X>sumW: P+=[[X-sumW,S]]
	for i in xrange(N):
		P+=[[W[i][1]-W[i][0],W[i][2]+S]]
	sortP(P)
	#if repeat+1==32: print P
	PR=[]
	while(t>0 and len(P)>0):
		#if repeat+1==32:
		#	print t
		#	print 1.*P[0][0]/(P[0][1]+R-S)
		if 1.*P[0][0]/(P[0][1]+R-S)<t:
			PR+=[[P[0][0],P[0][1]+R-S]]
			del(P[0])
			t-=1.*PR[len(PR)-1][0]/PR[len(PR)-1][1]
		else:
			PR+=[[(P[0][1]+R-S)*t,P[0][1]+R-S]]
			P[0][0]-=PR[len(PR)-1][0]
			if P[0][0]==0: del(P[0])
			t=0.
		#sortP(P)
	#if repeat+1==32: print X
	#if repeat+1==32 and len(P)>0: print P
	#f repeat+1==32 and len(PR)>0: print PR
	sumT=0.
	for i in xrange(len(P)):
		sumT+=1.*P[i][0]/P[i][1]
	for i in xrange(len(PR)):
		sumT+=1.*PR[i][0]/PR[i][1]
	print "Case #%d: %f" %(repeat+1,sumT)