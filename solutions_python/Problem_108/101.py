def next(n,length):
	if vines[n][1]==0: return True
	ls=[]
	for i in xrange(n+1,N+1):
		if vines[i][0]-vines[n][0]<=length:
			ls.append((i,min(vines[i][0]-vines[n][0],vines[i][1])))
		else: break
	ls.reverse()
	for item in ls:
		if next(item[0],item[1])==True: return True
	return False

T=int(raw_input())
for repeat in xrange(T):
	N=int(raw_input())
	vines=[]
	for t in xrange(N):
		line=raw_input().split()
		vines.append((int(line[0]),int(line[1])))
	vines.append((int(raw_input()),0))
	#print vines
	print "Case #%d:"%(repeat+1),
	if next(0,vines[0][0])==True: print "YES"
	else: print "NO"
