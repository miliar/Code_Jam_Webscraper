import math,string

maxT=int(raw_input().strip())
for T in xrange(maxT):
	numdin=int(raw_input().strip())
	inp=(raw_input().strip()).split()
	diners=[0]*1005
	for st in inp:
		diners[int(st)]+=1
	best=1005
	for i in xrange(1,1005):
		score=i
		for j in xrange(1005):
			score+=diners[j]*((j-1)/i)

		if(score<best):
			best=score
		
	print "Case #"+str(T+1)+": "+str(best)