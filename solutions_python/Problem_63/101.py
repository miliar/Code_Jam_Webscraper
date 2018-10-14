

finput = open("B-large.in","r")
foutput = open("B-large.out","w")	


def recurse(loadlist):
	if ( len(loadlist) == 1 ):
		return 1
	if (len(loadlist) ==  0):
		return 0
					
	length = len(loadlist)
	mid = length/2
	test_num = loadlist[mid]
	l_L = loadlist[:mid]
	l_R = loadlist[mid+1:]
	val = max ( recurse(l_L) , recurse(l_R) )
	return 1 + val
	
				 
	

T = int ( (finput.readline()).strip() )
lineno = 1

while ( T > 0) :
	inline = (finput.readline()).strip()
	splitline  = inline.split()
	L =  int(splitline[0])
	P =  int(splitline[1])
	C =  int(splitline[2])
	count = 0
	loadlist = []
	#loadlist.append(L)
	mul = C
	#print L,P,C ,mul 
	while ( L*mul < P ):
		#print L*mul
		loadlist.append(L*mul)
		mul = mul*C
	#loadlist.append(L*mul)			
			
			
	#print splitline
	
	#print loadlist 
	count  = recurse(loadlist)
	#print "ans  " , count
	
	

	
	
			
	s =  "Case #%s: %s\n" % ( lineno, count  )
	print s,
	foutput.write(s)
	
	lineno = lineno + 1	
	T = T - 1

    	









	    
    
