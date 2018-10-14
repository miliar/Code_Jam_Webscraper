f = open("input")

T = int(f.readline())

for tc in range(0, T):

	r = f.readline()
	s = r.split()



	Total = int(s[1])
	Written = int(s[0])

	ProbaMin      = 0.0 
	ProbaMinFound = False;
 
	s = f.readline()
	p1 = s.split()

	p = map(float, p1)
	
	for b in range(0, (Written + 1)):


		#print "= b"
		#print Written, b
		w = Written - b	
		loop = (1 << ((Written - b) )) - 1
				
		res = 0
		
		# backspace
		while (loop <> -1):

			failed = False
			proba = 1.0
			for i in range(0, w):
			
				if ((loop & 1 << i) == (1 << i)     ):
					proba = proba * p[i]
				else:
					proba = proba * (1 - p[i])
					failed = True
					
			#print "Loop"
			#print loop, failed	

			keystroke =  2 * b + (Total - Written) + 1
			if (failed):
				keystroke = keystroke + Total + 1
			res = res + keystroke * proba	
			#print keystroke
			#print proba
			#print res

			
			loop = loop - 1

		if (ProbaMinFound == False):
			ProbaMin = res
			ProbaMinFound = True
			ProbaMin = res
			#print "ProbaMin", ProbaMin
		else:
			if (ProbaMin > res):
				
				ProbaMin = res
				#print "ProbaMin", ProbaMin
	# enter
	keystroke = 1 + Total + 1
	res = keystroke
	
	if (ProbaMinFound == False):
		ProbaMin = res
		ProbaMinFound = True
		ProbaMin = res
		#print "ProbaMin", ProbaMin
	else:
		if (ProbaMin > res):
			ProbaMin = res
			ProbaMin = res
			#print "ProbaMin", ProbaMin
		
		
	print ("Case #%d: %.6f" % (tc + 1, ProbaMin))
		
			
			
			
			 
