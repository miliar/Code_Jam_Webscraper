

finput = open("C-small-attempt0.in","r")
foutput = open("C-small-attempt0.out","w")


T = int ( (finput.readline()).strip() )
lineno = 1
while ( T > 0) :
	# 1st line
	inline1 = (finput.readline()).strip()
	splitline1  = inline1.split()
	# 2nd line
	inline2 = (finput.readline()).strip()
	numlist  = inline2.split()

	R =  int(splitline1[0])
	k =  int(splitline1[1])
	N =  int(splitline1[2])
	
	for i in range(N):
		numlist[i] = int(numlist[i])
	numlist = [0] + numlist				
	#print R, k, N, numlist
	#print "initial numlist" , numlist
	#input sanitization over..now the actual code
	TotalEuros = 0
	roundNo = 0
	euros = 0
	
	while ( roundNo < R) :
		headcount = 0
		i = 0
		if numlist[i] == 0 and roundNo > 0 :
			TotalEuros = euros * ( (R - (R % roundNo)) /roundNo)
			R = R % roundNo  # set new R
			roundNo = 0
			euros = 0
			#print "here"
			continue
		headcount = numlist[0]
		while (headcount + numlist[(i+1)%(N+1)] <= k and i < N) :
			headcount = headcount + numlist[(i+1)%(N+1) ]
			#print "i here ", i+1, " = ", headcount
			i = i+1
		#print "I = ", i, "headcount = ", headcount
		numlist =  numlist[i+1:] + numlist[:i+1]
		#print numlist
		roundNo = roundNo + 1
		euros = euros + headcount
		#print euros
		
	TotalEuros = TotalEuros + euros
	
	s =  "Case #%s: %d\n" % ( lineno,TotalEuros )
	print s,
	foutput.write(s)
	
	lineno = lineno + 1	
	T = T - 1

    	









	    
    
