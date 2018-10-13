T = int(raw_input())

for t in xrange(T):
        VS=0
        VSS=0
        S = 0
        N = 0
	M,L = raw_input().split()
	M = int(M)
	VSS += int(L[0])
	
	for m in range(1,M+1):
		
		if m >= VSS and int(L[m])>0:
			VS += (m - VSS)
			VSS += (m - VSS)+int(L[m]) 
		elif m < VSS and int(L[m])>0:
			VSS +=int(L[m])
	print "Case #%d: %d" % (t + 1, VS)


	        
