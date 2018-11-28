import sys,os

def getline():
	return sys.stdin.readline().rstrip()

T = int(getline())

for case in range(1, T+1):
	row = [ int(x) for x in getline().split() ]
	N,S,p = row[:3]
	t = row[3:]
	res = 0
	nsp = 3*(p-1) + 1
	sp = max(1,3*(p-2) + 2)
	for x in t:
		if x >= nsp: 
			res+=1
		elif S and x >= sp:
			S-=1
			res+=1
	print "Case #%d: %d" % (case,res)
