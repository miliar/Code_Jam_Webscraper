#this function return set of search engines
def getse():
	se =()
	searchengines = int( f.readline().split('\n')[0] )
	for i in range( 0 ,  searchengines ):
		se += ( f.readline().split('\n')[0] , )
	return se

#this function return list of queries
def getq_list():
	q = [] 
	queries = int( f.readline().split('\n')[0] ) 
	for i in range( 0 , queries ):
		q.append( f.readline().split('\n')[0] )
	return q
		
#here we are starting 
f = open('A-large.in', 'r')
testcases = int( f.readline().split('\n')[0] )
for i in range(0,testcases):	

	#aquire data into memory from one task
	seset = getse()
	querylist = getq_list()
	
	
	if len(querylist) == 0:
		print "Case #%d: %d" % ( i + 1 , 0 )
		continue
		
	cdict = {}		
	for se in seset:
		plot = []
		level=0
		for n in querylist:
			if ( n == se ):
				level = 0
			else:
				level = level  + 1
			plot.append( level )
				
		plot.reverse()
		prev = plot[0]
		for n in range(0,len(plot)):
			if plot[n] == 0:
				prev = 0
			else:
				if ( plot[n] < prev ):				
					plot[n] = prev 
				else:
					prev = plot[n] 
					
		plot.reverse()
		
		step = 0 
		for n in range(0,len(plot)):
			if plot[n] != 0:
				plot[n] = plot[n] - step
				step = step + 1
			else:
				step = 0
		
		
		cdict[se]= plot
		

	#routing 
	switchcount = 0
	candidate = ""
	for pos in range(0,len(querylist)):
		if ( candidate == "" ):
			max = 0
			for se in seset:
				maxxy = cdict[ se ][pos]
				if ( maxxy > max ):
					max = maxxy
					candidate = se

		else:
			if ( cdict[ candidate ][pos]  == 0 ) :
				switchcount = switchcount + 1 
				max = 0 
				for se in seset:
					maxxy = cdict[ se ][pos]
					if ( maxxy > max ):
						max = maxxy
						candidate = se						
		
	print "Case #%d: %d" % ( i + 1 , switchcount )
	
