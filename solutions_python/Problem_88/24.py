import sys

file = open("B-small-attempt0.in")
#file = open("b.test")
strWholeFile = file.read()
aStrLines = strWholeFile.split("\n")

nCases = int(aStrLines[0])
aStrLinesLeft = aStrLines[1:]

for nCase in range(1, nCases + 1):
	print >> sys.stderr, "On case " + str(nCase) + " of " + str(nCases)

	aStrTok = aStrLinesLeft[0].split()
	
	rMax = int(aStrTok[0])
	cMax = int(aStrTok[1])
	w = float(aStrTok[2])
	
	print >> sys.stderr, aStrLinesLeft[1:rMax]
	aryW = map(lambda rCur: map(lambda cCur: aStrLinesLeft[rCur+1][cCur], range(cMax)), range(rMax))
	
	aStrLinesLeft = aStrLinesLeft[rMax+1:]
	
	n = min(rMax, cMax)
	fSolved = False
	
	while n >= 3:
		#print >> sys.stderr, "Trying n=" + str(n)
		for rStart in range(0, rMax - n + 1):
			if fSolved:
				break
			for cStart in range(0, cMax - n + 1):
				rCenter = float(rStart) + float(n-1) / 2.0
				cCenter = float(cStart) + float(n-1) / 2.0
				rBalance = 0.0
				cBalance = 0.0
				
				rEnd = rStart + n - 1
				cEnd = cStart + n - 1
				
				for r in range(rStart, rStart + n):
					for c in range(cStart, cStart + n):
						if (r == rEnd or r == rStart) and (c == cEnd or c == cStart):
							continue
						
						dR = float(r) - rCenter
						rBalance += dR * (float(aryW[r][c]) + w)
						
						dC = float(c) - cCenter
						cBalance += dC * (float(aryW[r][c]) + w)
				
				#print >> sys.stderr, "Blade at " + str(rStart) + ", " + str(cStart) + "; balance is " + str(rBalance) + ", " + str(cBalance)
				if rBalance == 0.0 and cBalance == 0.0:
					fSolved = True
					break
		
		if fSolved:
			break
		n -= 1
	if n >= 3:
		print "Case #" + str(nCase) + ": " + str(n)
	else:
		print "Case #" + str(nCase) + ": IMPOSSIBLE"