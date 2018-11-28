from sys import *

def solve(i, R, k, G):
	
	counter = 0
	riders = []
	
	total_G = reduce(lambda x,y: x+y, G)
	if(total_G<=k):
		print "Case #%d: %s" %(i+1, total_G*R)
		return
	
	for x in xrange(R): 
		#print "Group at Round %d: %s" % (R, G[0])
		if(G[0] > k):
			print "Case #%d: %s" %(i+1, counter)
			return
		
		tmp = 0
		while(len(G)>0 and tmp + G[0] <=k):
			group = G[0]
			tmp = tmp + group
			G = G[1:]
			riders.append(group)
		#print "Riders at Round %d: %s" % (R, riders)	
		counter = counter + reduce(lambda x,y: x+y, riders)
		G.extend(riders)
		riders = []
		#print "Queue at End of Round %d: %s" % (R, G)
	
	print "Case #%d: %s" %(i+1, counter)
	

n_cases = int(raw_input())
for i in xrange(n_cases):
	R, k, N =  map(int, stdin.readline().split())
	G = map(int, stdin.readline().split())
	
	if(N==1):
		if G[0] <= k:
			print "Case #%d: %s" %(i+1, G[0]*R)
		else:
			print "Case #%d: %s" %(i+1, 0)
		continue
	
	solve(i, R, k, G)