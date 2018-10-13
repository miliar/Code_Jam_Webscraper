

finput = open("A-large.in","r")
foutput = open("A-large.out","w")


T = int ( (finput.readline()).strip() )
lineno = 1
while ( T > 0) :
	inline = (finput.readline()).strip()
	splitline  = inline.split()
	N =  int(splitline[0])
	K =  int(splitline[1])
	
	if (K==0):
		s =  "Case #%s: OFF\n" % ( lineno )
		print s,
		foutput.write(s)
		lineno = lineno + 1	
		T = T - 1
		continue
	if ( (K+1) % (2**N) == 0)	:
		s =  "Case #%s: ON\n" % ( lineno )
		print s,
		foutput.write(s)
		lineno = lineno + 1	
		T = T - 1
		continue
			
	s =  "Case #%s: OFF\n" % ( lineno )
	print s,
	foutput.write(s)
	
	lineno = lineno + 1	
	T = T - 1

    	









	    
    
