import math,string

maxT=int(raw_input().strip())
for T in xrange(maxT):
	aud=[]
	inp=(raw_input().strip()).split()
	maxshy=int(inp[0])
	for i in range(maxshy+1):
		aud.append(int(inp[1][i]))
	standing=0
	needed=0
	for i in range(maxshy+1):
		if standing<i:
			needed+=1
			standing+=1
		standing+=aud[i]
	print "Case #"+str(T+1)+": "+str(needed)

