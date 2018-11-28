import sys

def iterate(k,gj):
	tc = 0
	i = 0
	max = None
	for j in gj:
		if tc +j <= k :
			tc +=j
			max = i
		else :
			break
		i += 1
	gj = gj[max+1:]+gj[0:max+1] 
	return gj, tc

def process(i,R,k,gj) :
	money = 0
	for x in xrange(0,R):
		gj, moneyIt = iterate(k,gj)
		money += moneyIt
	return "Case #%d: %d" % (i,money) 
	
i = 0
caseCount = 0
R = None
k = None
N = None
for line in file(sys.argv[1]):
	if i == 0:
		i += 1
		continue
	if i % 2 == 1:
		(R,k,N) = map(lambda x:int(x), line.split(" "))
	else :
		gj = map(lambda x:long(x), line.split(" "))
		caseCount += 1
		print process(caseCount,R,k,gj)
	i += 1