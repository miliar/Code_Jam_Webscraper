#

T = int( raw_input() )

for t in xrange( 1, T+1 ):
	
	R, k, N = map( int, raw_input().split() )
	
	gs = map( int, raw_input().split() )
	jump = [0]*N
	cost = [0]*N
	
	for i in xrange( N ):
		
		j = i+1
		s = gs[i]
		
		if j >= N:
			
			j -= N
		
		while s+gs[j] <= k and j != i:
			
			s += gs[j]
			j += 1
			
			if j >= N:
				
				j -= N
		
		jump[i] = j
		cost[i] = s
	
	total = 0
	c = 0
	
	seen = {}
	
	r = 0
	while r < R:
		
		total += cost[c]
		
		if c in seen:
			
			remaining = R-1-r
			
			oldTotal, oldIndex = seen[c]
			
			loopTotal = total-oldTotal
			loopLength = r-oldIndex
			
			total = total+loopTotal*(remaining/loopLength)
			
			#print "init remaining", remaining
			#print "loop length", loopLength
			#print "loop value", loopTotal
			#print "loops done", remaining/loopLength
			#print "now remaining", remaining%loopLength 
			
			r = R-1-(remaining%loopLength)
			seen = {}
		
		else:
			
			seen[c] = (total,r)
		
		c = jump[c]
		r += 1
	
	print "Case #%d:" % t, total

