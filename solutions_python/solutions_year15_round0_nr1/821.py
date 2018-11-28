import sys
import numpy as np

def barrier(audience):
	level = 0;
	for i in range(len(audience)):
		if i <= level:
			level += audience[i]
		else:
			break

	audience = audience[level:]
	bar = 0;
	if len(audience)>0:
		bar = np.where(np.array(audience)!=0)[0][0]

	return audience,bar

def numfriends(line):
	audience = [int(s) for s in list(line[1])]
	additions = 0
	audience,bar = barrier(audience)
	while len(audience)>0:
		audience[0]=bar
		additions+=bar 
		audience,bar=barrier(audience)
		
	return additions

infilename = sys.argv[1]
f=open(infilename,'r')
numlines = int(f.readline())

for i in range(numlines):
	line=f.readline().split()
	print "Case #"+str(i+1)+": "+str(numfriends(line))








