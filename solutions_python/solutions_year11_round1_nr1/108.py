import sys


n = 0

for line in sys.stdin:
	if n == 0:
		n = 1
		continue
	
	word = line.split()
	nN = int(word[0])
	pD = int(word[1])
	pG = int(word[2])
	
	nflg = 1
	
	if(pG == 100):
		if(pD != 100):
			nflg = 0
	elif(pG == 0):
		if(pD != 0):
			nflg = 0
	else:
		nflg = 0
		if nN > 100:
			nN = 100
		for x in range(1,nN+1):
			dX = float(x) * pD / 100.0
			nX = int(dX)
			if dX == nX:
				nflg = 1
				break
	
	if(nflg == 1):
		outstr = "Possible" 
	else :
		outstr = "Broken" 
		
	print "Case #" + str(n) + ": " + outstr
	n+= 1