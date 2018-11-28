#! /usr/bin/env python

fin = open("large.in","r")

cases = fin.readline().rstrip("\n")

for case in xrange(int(cases)):
	goodList = []
	(N,K,B,T) = fin.readline().rstrip("\n").split(" ")
	distList = fin.readline().rstrip("\n").split(" ")
	timeList = fin.readline().rstrip("\n").split(" ")

	for (a,(i,j)) in enumerate(zip(distList,timeList)):
		sum = ( int(j)*int(T) ) + int(i)
		#print sum
		if sum >= int(B): goodList.append(a)

	#print goodList	
	#print len(goodList)
	#print K

	more = 0
	if len(goodList) >= int(K):
		newList = list(reversed(goodList))
		for x,i in enumerate(newList[:int(K)]):
			more = more + int(N) - 1 - x - i
	else:
		more = "IMPOSSIBLE"

	print "Case #" + str(case+1) + ": " + str(more)

fin.close()